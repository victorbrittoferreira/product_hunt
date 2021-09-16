from django.shortcuts import render

#from .models import Products

#import.models

def home (request):
    return render(request, 'products/home.html')

