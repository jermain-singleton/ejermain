from django.shortcuts import render

# Create your views here.

def home(request):
    """The home page for my portfolio"""
    return render(request, 'index.html')