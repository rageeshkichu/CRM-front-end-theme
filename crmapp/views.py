from django.shortcuts import render
from django.http import JsonResponse
from urllib.parse import unquote
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def navbar(request):
    return render(request,'navbar.html')

def home(request):
    return render(request,'home.html')

def cards(request):
    return render(request,'cards.html')

def navbar2(request):
    return render(request,'navbar2.html')


def dash(request):
    # Retrieve the dragged card's HTML from the URL parameter
    dragged_html_encoded = request.GET.get('draggedHTML', None)
    dragged_html = unquote(dragged_html_encoded) if dragged_html_encoded else None
    return render(request, 'dash.html', {'dragged_html': dragged_html})
