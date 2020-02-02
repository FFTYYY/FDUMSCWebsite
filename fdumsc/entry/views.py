from django.shortcuts import render , HttpResponse


def index(request):
	return HttpResponse("""
		<a href="/articles"> 文章 </a>
		<p></p>
		<a href="/forum"> 讨论区 </a>
	""")