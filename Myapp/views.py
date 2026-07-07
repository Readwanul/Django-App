from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('<h1>Hello, world. You\'re at the Myapp index.</h1>')

def about(request):
    return HttpResponse('<h3>I am <I> Readwan </I> </h3>')