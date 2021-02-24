from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'helper/list-request.html')


def review(request):
    return render(request, 'helper/list-request.html')


def add(request):
    return render(request, 'helper/questions_adder.html')