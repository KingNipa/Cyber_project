from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Product, Order
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import logout
# from .forms import BuyProductForm  #Flaw 2: lets use form!

def home(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})

def login_view(request):
    next_url = request.GET.get('next') or ''
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        next_url = request.POST.get('next', next_url)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "you signed in!")
            if next_url:
                return redirect(next_url)
            else:
                return redirect('home')
        else:
            messages.error(request, "wrong username or password.")
    return render(request, 'store/login.html', {'next': next_url})

def logout_view(request):
    logout(request)
    messages.success(request, "You are logged out.")
    return redirect('home')    


#bad version flaw 1:
def orders_view(request, user_id):
    orders = Order.objects.filter(user_id=user_id)
    return render(request, 'store/orders.html', {'orders': orders})

# Flaw 1: better version: 
'''
@login_required(login_url='login')
def orders_view(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'store/orders.html', {'orders': orders})
'''

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'store/product_detail.html', {'product': product})

#Flaw 1: bad version:
def all_orders_view(request):
    orders = Order.objects.all()
    return render(request, 'store/orders.html', {'orders': orders})    
'''
# Flaw 1: better version:  
@login_required(login_url='login')
def all_orders_view(request):
    if not request.user.is_staff:
        return redirect('home')  #home if no orders
    orders = Order.objects.all()
    return render(request, 'store/orders.html', {'orders': orders})
'''   

#Flaw 2: This is poorly done:
@login_required(login_url='login') 
def buy_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
     
    if request.method == 'POST':
        # buyer informations:
        buyer_name = request.POST.get('buyer_name')
        buyer_email = request.POST.get('buyer_email')
        buyer_address = request.POST.get('buyer_address')
        buyer_phone = request.POST.get('buyer_phone')
        
        # create order
        Order.objects.create(
            user=request.user,
            product=product,
            quantity=1,
            buyer_name=buyer_name,
            buyer_email=buyer_email,
            buyer_address=buyer_address,
            buyer_phone=buyer_phone
        )
        messages.success(request, f"You bought {product.name}!")
        
        return redirect('orders', user_id=request.user.id) #in fixed version Flaw 1: return redirect('orders')
    else:
        return render(request, 'store/buy_product.html', {'product': product})

'''
#Flaw 2: Better version:
@login_required(login_url='login')
def buy_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = BuyProductForm(request.POST)
        if form.is_valid():
            Order.objects.create(
                user=request.user,
                product=product,
                quantity=1,
                buyer_name=form.cleaned_data['buyer_name'],
                buyer_email=form.cleaned_data['buyer_email'],
                buyer_address=form.cleaned_data['buyer_address'],
                buyer_phone=form.cleaned_data.get('buyer_phone', '')
            )
            messages.success(request, f"You bought {product.name}!")
            return redirect('orders')
    else:
        form = BuyProductForm()
    return render(request, 'store/buy_product.html', {'product': product, 'form': form})     
'''