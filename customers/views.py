from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from .models import Customer
from .forms import CustomerMultiForm


class CustomerView(ListView):
    model = Customer
    template_name = 'customers/customers.html'
    context_object_name = 'customers'
    ordering = ['-date_modified']
    paginate_by = 10

class AddCustomerView(CreateView):
    form_class = CustomerMultiForm
    success_url = '/customers'
    template_name = 'customers/add_customer.html'

    def form_valid(self, form):
        address = form['address'].save()
        customer = form['customer'].save(commit=False)
        customer.address = address
        customer.save()
        return redirect(self.success_url)

