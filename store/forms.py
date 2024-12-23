'''
from django import forms
#This file is not used on the original site but is related to fixing flaw 2!
class BuyProductForm(forms.Form):
    buyer_name = forms.CharField(max_length=60)
    buyer_email = forms.EmailField(max_length=60)
    buyer_address = forms.CharField(max_length=60)
    buyer_phone = forms.CharField(max_length=60, required=False)
'''


#To fix flaw 2 we need to use forms to validate that bad people can't write scripts in the input fields.
#And as an additional note that "EmailField" is a little extra security for user misspelling.