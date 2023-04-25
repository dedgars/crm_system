from django.shortcuts import render
from django.views.generic import ListView
from .models import Customer


class CustomerView(ListView):
    model = Customer
    template_name = 'customers/customers.html'
    context_object_name = 'customers'
    ordering = ['-date_modified']
    paginate_by = 10

