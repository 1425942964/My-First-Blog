# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def hackerrank(request):
	return render(request, 'blog/hackerrank.html')

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts':posts})
	
def introduction(request):
	return render(request, 'blog/introduction.html')

def contact(request):
	return render(request, 'blog/contact.html')

def hello(request):
	return render(request, 'blog/hello.html')