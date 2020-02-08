from ..models import Visitor
from .cookie_control import make_cookie_value , ask_cookie_value , set_cookie_value , del_cookie
from django.http import HttpResponse , Http404

authorization_key = "FDUMSC_LOGEDIN"


def ask_visitor(request):
	'''输入一个request，返回这个request对应的visitor

	:param request: 一个用户请求
	:return: 一个Visitor对象。如果用户没有注册，则返回None
	'''

	cookie_val = ask_cookie_value(request , authorization_key)

	if cookie_val is not None:
		visitor = Visitor.objects.filter(cookie_value = cookie_val)
	else: 
		visitor = []

	if len(visitor) <= 0:
		visitor = None
	else:
		visitor = visitor[0]

	return visitor

def visitor_signin(visitor , response = None):
	'''将一个visitor的状态设为登录。
	可以提供一个登录成功的response，如果不提供，则会默认提供一个

	:response: 一个Visitor对象，表述要登录的用户
	:param response: 一个响应
	:return: response
	'''
	if response is None:
		response = HttpResponse("<p>登录成功！</p>")

	set_cookie_value(response , authorization_key , visitor.cookie_value)

	return response

def visitor_signout(visitor , response = None):
	'''取消一个visitor的登录状态
	可以提供一个登录成功的response，如果不提供，则会默认提供一个

	:param response: 一个响应
	:return: 一个Visitor对象。
	'''

	if response is None:
		response = HttpResponse("<p>注销成功！</p>")

	del_cookie(response , authorization_key)

	return response
