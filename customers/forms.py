
from django import forms
from .models import Address, Customer
from betterforms.multiform import MultiModelForm


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ['customer_type', 
                  'first_name', 
                  'last_name', 
                  'organization_name', 
                  'organization_registration_number', 
                  'organization_vat_number', 
                  'email', 
                  'phone']

class CustomerMultiForm(MultiModelForm):
    
    form_classes = {
        'customer': CustomerForm,
        'address': AddressForm,
    }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            # visible.field.widget.attrs['placeholder'] = visible.field.label
        


