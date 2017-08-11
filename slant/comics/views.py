from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Comic

# Create your views here.

#@login_required
def index(request):
  comic = Comic.objects.all().first()
  return render(request, 'comics/index.html', {'comic': comic})

#@login_required
def check_for_new(request):
  comic = Comic.check_for_new()
  return render(request, 'comics/comic.html', {'comic': comic})

#@login_required
def get_random(request):
  comic = Comic.get_random()
  return render(request, 'comics/comic.html', {'comic': comic})
