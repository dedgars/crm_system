
from django.urls import path
from django.views.generic import TemplateView, RedirectView
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'equipment'

urlpatterns = [
    path('equipment', login_required(views.EquipmetView.as_view()), name='equipment'),
    path('add_equipment/<int:customer_id>', views.AddEquipmentView.as_view(), name='add_equipment'), 
]
