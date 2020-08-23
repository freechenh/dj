from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here.
def hello(request):
    return HttpResponse(r'<h1>hello world')


def person(request):
    return


def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html')
