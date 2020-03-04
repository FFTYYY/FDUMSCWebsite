from django.shortcuts import render , HttpResponse
from authorization.utils.visitor_control import ask_visitor

def index(request):

	now_visitor = ask_visitor(request)

	visitor_name = "游客" if now_visitor is None else now_visitor.name
	# 三对引号的目的是包含多行html代码
	return HttpResponse("""
		<p>当前登录用户: %s
		<p></p>
		<a href="/articles"> 文章 </a><br/>
		<a href="/forum"> 讨论区 </a><br/>

		<a href="/authorization/signin"> 登录 </a><br/>
		<a href="/authorization/signup"> 注册 </a><br/>
		<a href="/authorization/signout"> 注销 </a><br/>

	""" % (visitor_name))