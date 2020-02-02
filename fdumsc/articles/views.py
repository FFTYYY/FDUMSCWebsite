from django.shortcuts import render , HttpResponse
from .models import Article , Comment

def index(request):

	artiles = Article.objects.all()

	return render(request , "articles/index.html" , {
		"article_list" : artiles
	})

def get_article(request , article_address):

	article = Article.objects.filter(address = article_address)[0]

	return render(request , "articles/article.html" , {
		"content" : article.content , 
		"title" : article.title , 
	})


def upload_comment(request , article_address):
	pass
	# TODO