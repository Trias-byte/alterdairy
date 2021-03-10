from django.shortcuts import render
from django.views.generic import DetailView
from .models import Peaples
#  from .account import Users
# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def log(request):
    return render(request, 'main/entered.html')