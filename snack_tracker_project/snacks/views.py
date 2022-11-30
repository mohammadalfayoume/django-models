from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.
from .models import Snack

class SnackListView(ListView):
    template_name= 'snack_list.html'
    model= Snack
    