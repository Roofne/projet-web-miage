from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

def about(request):
    return render(request, 'about.html')

def login(request):
    return render(request, 'login.html')
