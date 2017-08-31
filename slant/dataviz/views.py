from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Story

# Create your views here.

#@login_required
def index(request):
  stories_list = Story.objects.all().order_by('rank')
  context = { 'stories_list': stories_list }
  return render(request, 'dataviz/splash.html', context)

#@login_required
def detail(request, slug):
  story = get_object_or_404(Story, slug=slug)
  context = {
      'story': story,
      }
  return render(request, 'dataviz/detail.html', context)
