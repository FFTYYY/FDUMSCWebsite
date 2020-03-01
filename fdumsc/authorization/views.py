'''
每个用户注册之后会给这个用户分配一个独特的cookie value
当一个用户登录时就会给他的浏览器发一个cookie，当退出登录时就会删除这个cookie。
每次获得request，可以通过检查是否有cookie来判断是否登录，通过cookie value来判断是哪个用户

'''

from django.http import HttpResponse , Http404
from django.template import loader
from django.shortcuts import render , get_object_or_404
import django.http as http
from .models import Visitor
from .utils.visitor_control import ask_visitor , visitor_signin , visitor_signout

def sign_up(request):
	return render(request , "authorization/signup.html" , {
	})


def sign_up_submit(request):

	if request.POST:
		name_id = request.POST.get('name_id')
		name = request.POST.get('name')
		email = request.POST.get('email')
		password = request.POST.get('password')

		visitor = Visitor(name = name , name_id = name_id , email = email , password = password)
		visitor.save()


	return http.HttpResponseRedirect("../../")

def sign_in_submit(request):
	
	response = http.HttpResponseRedirect("../../")

	if request.POST:
		name_id = request.POST.get('name_id')
		password = request.POST.get('password')

		visitor = Visitor.objects.filter(name_id = name_id , password = password)
		if len(visitor) <= 0:
			return HttpResponse("名或密码错误")

		visitor = visitor[0]

		response = visitor_signin(visitor , response)

	return response

def sign_out(request):

	visitor = ask_visitor(request)

	if visitor is None:
		return HttpResponse("没有登录吖")

	response = render(request , "authorization/signout.html" , {
	})

	response = visitor_signout(visitor , response = response)

	return response



def sign_in(request):

	return render(request , "authorization/signin.html" , {
	})
