from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Project

# Create your views here.

#@login_required
def index(request):
  proj_list = Project.objects.all().order_by('rank')
  context = { 'projects_list': proj_list }
  return render(request, 'portfolio/splash.html', context)

#@login_required
def detail(request, slug):
  proj = get_object_or_404(Project, slug=slug)
  context = {
      'project': project,
      }
  return render(request, 'portfolio/detail.html', context)
