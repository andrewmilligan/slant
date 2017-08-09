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
  Comic.check_for_new()
  return redirect('comics:index')
