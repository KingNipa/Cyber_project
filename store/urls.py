from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('buy/<int:product_id>/', views.buy_product, name='buy_product'),
    path('orders/<int:user_id>/', views.orders_view, name='orders'), # Flaw 1 fixed version: path('orders/', views.orders_view, name='orders'),
    path('logout/', views.logout_view, name='logout'),
    path('orders/', views.all_orders_view, name='all_orders'), #Flaw 1 fix: check permissions in views.py: def all_orders_view
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)