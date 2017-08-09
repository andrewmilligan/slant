from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Story

# Create your views here.

#@login_required
def index(request):
  image_stories_list = Story.objects.filter(
      images__isnull=False).distinct().order_by('-creation_date')
  no_image_stories_list = Story.objects.filter(
      images__isnull=True).distinct().order_by('-creation_date')
  context = { 'image_stories_list': image_stories_list,
               'no_image_stories_list': no_image_stories_list }
  return render(request, 'stories/index.html', context)

#@login_required
def detail(request, pk):
  story = get_object_or_404(Story, pk=pk)
  return render(request, 'stories/detail.html', {'story': story})

#@login_required
def check_for_new(request):
  Story.check_for_new()
  return redirect('stories:index')
