from django.shortcuts import render
from django.http import HttpResponse

def page2(request):
    return render(request, 'Page2.html')

def page3(request):
    return HttpResponse("This is page 3 of App2.")

def page4(request):
    return HttpResponse("This is page 4 of App2.")

# Create your views here.
