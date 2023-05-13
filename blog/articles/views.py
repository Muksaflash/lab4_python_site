# -*- coding: utf-8 -*-

from .models import Article
from django.shortcuts import render
from django.http import Http404

def archive(request):
	return render(request, 'archive.html', {"posts": Article.objects.all()})

def get_article(request, article_id):
	try:
		post = Article.objects.get(id=article_id)
		print(f"post: {post}")
		return render(request, 'article.html', {"post": post})
	except Article.DoesNotExist:
		print("Article.DoesNotExist")
		raise Http404

