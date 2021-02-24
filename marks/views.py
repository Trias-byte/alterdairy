from django.shortcuts import render


def index(request):
    return render(request, 'marks/marks-list.html')
