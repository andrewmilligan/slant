from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
import random

from .models import Tweet

# Create your views here.

#@login_required
def index(request):
  #tweets_list = Tweet.objects.all()
  tweets_list = sorted(Tweet.objects.all().order_by('id'),
      key=lambda x: random.random())
  random.shuffle(tweets_list)
  context = { 'tweets_list': tweets_list }
  return render(request, 'feed/index.html', context)
