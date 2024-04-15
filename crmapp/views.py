from django.shortcuts import render

# Create your views here.

def navbar(request):
    return render(request,'navbar.html')

def home(request):
    return render(request,'home.html')

def home2(request):
    return render(request,'home2.html')

def dash(request):
    return render(request,'dash.html')
