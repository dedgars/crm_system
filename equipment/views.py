from django.shortcuts import render
from django.views.generic import ListView
from .models import Equipment


class EquipmetView(ListView):
    model = Equipment
    template_name = 'equipment/equipment.html'
    ordering = ['-date_modified']
    paginate_by = 10