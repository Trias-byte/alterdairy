from django.shortcuts import render
from django.views.generic import DetailView
from .models import Peaples
# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def status(request):
    pass


def log(request):
    return render(request, 'main/entered.html')