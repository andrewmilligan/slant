from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Story

# Create your views here.

#@login_required
def index(request):
  stories_list = Story.objects.all()
  context = { 'stories_list': stories_list }
  return render(request, 'dataviz/index.html', context)

#@login_required
def detail(request, pk):
  story = get_object_or_404(Story, pk=pk)
  context = {
      'story': story,
      }
  return render(request, 'dataviz/detail.html', context)

#@login_required
def check_for_new(request):
  Story.check_for_new()
  return redirect('dataviz:index')
