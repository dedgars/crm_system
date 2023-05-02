
from django import forms
from betterforms.multiform import MultiModelForm

from .models import Equipment
from customers.forms import AddressForm


class EquipmentForm(forms.ModelForm):
    
    choose_address = forms.BooleanField(initial=True, required=False, label="Use customer address.")
    
    class Meta:
        model = Equipment
        fields = ['type', 'brand', 'model', 'serial_number', 'description', 'installation_date']

        widgets = {
            'installation_date': forms.DateInput(attrs={'type': 'date'})
            }
        

class EquipmentMultiForm(MultiModelForm):


    
    form_classes = {
        'equipment': EquipmentForm,
        'address': AddressForm,
    }



