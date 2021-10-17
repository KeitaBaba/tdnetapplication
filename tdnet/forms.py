from django import forms
from .models import Customer,Code


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('customer','customer_address')

class CodeForm(forms.ModelForm):
    class Meta:
      model = Code
      fields = ('customer','code')