from typing import Any, Dict
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, View
from .models import Customer, Address
from equipment.models import Equipment
from .forms import CustomerMultiForm, AddressForm, CustomerForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required


class CustomerView(ListView):
    model = Customer
    template_name = 'customers/customers.html'
    context_object_name = 'customers'
    ordering = ['-date_modified']
    paginate_by = 10

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customers/customer_detail.html'
    context_object_name = 'customer'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['equipment'] = Equipment.objects.filter(customer=self.object)
        return context

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

class EditCustomerView(UpdateView):
    model = Customer
    fields = [
        'customer_type', 'first_name', 'last_name', 'organization_name', 'organization_registration_number', 
        'organization_vat_number', 'email', 'phone']
    success_url = '/customers'
    template_name = 'customers/edit_customer.html'

class EditAddressView(UpdateView):
    model = Address
    fields = "__all__"
    success_url = '/customers'
    template_name = 'customers/edit_address.html'

class DeleteCustomerView(DeleteView):
    model = Customer
    success_url = '/customers'
    template_name = 'customers/delete_customer.html'
    context_object_name = 'customer'


@login_required
def search_customers(request):
    return render(request, 'customers/search_customers.html')


@login_required
def search(request):
    search_term = request.POST.get('search', None)
    if search_term:
        results = Customer.objects.filter(
            Q(first_name__icontains=search_term) | 
            Q(last_name__icontains=search_term) | 
            Q(address__street_name__icontains=search_term) | 
            Q(email__icontains=search_term) | 
            Q(organization_name__icontains=search_term)
            )
              
        context = {'results': results}
    else:
        context = {}
    return render(request, 'customers/search_results.html', context)
