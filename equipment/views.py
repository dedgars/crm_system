from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from .models import Equipment
from customers.models import Customer
from .forms import EquipmentMultiForm


class EquipmetView(ListView):
    model = Equipment
    template_name = 'equipment/equipment.html'
    ordering = ['-date_modified']
    paginate_by = 10

class AddEquipmentView(CreateView):
    model = Equipment
    template_name = 'equipment/add_equipment.html'
    form_class = EquipmentMultiForm

    def form_valid(self, form):
        if form['equipment'].cleaned_data['choose_address'] == True:
            appliance = form['equipment'].save(commit=False)
            appliance.customer = Customer.objects.get(pk=self.kwargs['customer_id'])
            appliance.address = Customer.objects.get(pk=self.kwargs['customer_id']).address
        else:  
            address = form['address'].save()
            appliance = form['equipment'].save(commit=False)
            appliance.address = address
            appliance.customer = Customer.objects.get(pk=self.kwargs['customer_id'])
        appliance.save()
        return redirect('/view/{}'.format(self.kwargs['customer_id']))


