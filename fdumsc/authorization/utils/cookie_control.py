import random

def make_cookie_value(length = 20):
	'''生成一个随机字符串
	'''
	return "".join(["%d" % (random.randint(0,9)) for i in range(length)])

def ask_cookie_value(request , key):
	'''输入一个request，返回这个request对应的cookie值

	:param request: 一个用户请求
	:param str key: cookie名 
	:return str: 这个请求的名为key的cookie的值，不存在则返回None
	'''
	return request.COOKIES.get(key)

def set_cookie_value(response , key , value = None):
	'''给用户设置cookie值

	:param response: 一个网站响应
	:param str key: cookie名 
	:param str value: cookie值
	:return response: 返回输入的response
	'''
	response.set_cookie(
		key = key ,
		value = value ,
		max_age = 60 * 60 * 24 * 365 * 100 , #每过一百年就得重新获取一次
		#domain =  domain,
		#path = "/" , 
	)
	return response

def del_cookie(response , key):
	response.delete_cookie(key)
