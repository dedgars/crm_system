
from django.urls import path
from django.views.generic import TemplateView, RedirectView
from . import views

from . import views

app_name = 'customers'

urlpatterns = [
    path('', views.CustomerView.as_view(), name='customers'),
]