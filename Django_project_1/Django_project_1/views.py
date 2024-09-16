from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, world. You are at Django Prject 1 Home Page")
    return render(request, 'website/index.html')

def about(request):
    # return HttpResponse("Hello, world. You are at Django Project1 About Page")
    return render(request, 'website/about.html')

def contact(request):
    # return HttpResponse("Hello, world. You are at Django Project 1 Contact Page")
    return render(request, 'website/contact.html')