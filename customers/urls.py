
from django.urls import path
from django.views.generic import TemplateView, RedirectView
from . import views
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'customers'

urlpatterns = [
    path('', login_required(views.CustomerView.as_view()), name='customers'),
    path('customers', login_required(views.CustomerView.as_view()), name='customers'),
    path('add/', login_required(views.AddCustomerView.as_view()), name='add_customer'),
    path('edit/<int:pk>/', login_required(views.EditCustomerView.as_view()), name='edit_customer'),
    path('edit_address/<int:pk>/', login_required(views.EditAddressView.as_view()), name='edit_address'),
    path('delete/<int:pk>/', login_required(views.DeleteCustomerView.as_view()), name='delete_customer'),
    path('view/<int:pk>/', login_required(views.CustomerDetailView.as_view()), name='customer_detail'),
    path('search_customers', views.search_customers, name='search_customers'),
    path('search_results', views.search, name='search_results'),

]

