from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
  return render(request, 'general/home.html')

def about(request):
  return render(request, 'general/about.html')
