
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
]

