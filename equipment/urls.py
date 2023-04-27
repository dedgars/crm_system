
from django.urls import path
from django.views.generic import TemplateView, RedirectView
from . import views
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'equipment'

urlpatterns = [
    path('equipment', login_required(views.EquipmetView.as_view()), name='equipment'),
]
