from django.shortcuts import render
from django.views.generic import DetailView
from .models import RequestsHelps


# Create your views here.


def index(request):
    questions = RequestsHelps.objects.all()
    return render(request, 'helper/list-request.html', {'questions_list': questions})


class Detail(DetailView):
    model = RequestsHelps
    template_name = 'helper/detail.html'
    context_object_name = 'question'


def add(request):
    return render(request, 'helper/questions_adder.html')