from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import Http404
import django.http as http
from .models import *
import os
import django.utils.timezone as timezone
import copy
from authorization.utils import visitor_control

def index(request):
	return http.HttpResponseRedirect("./main")

def get_board(request , board_address):

	board = Board.objects.get(address = board_address)

	return render(request , "forum/board.html" , {
		"board" : board,
		"friend_list" : board.friends.all(),
		"topic_list" : board.topics.all(),
	})

def get_topic(request , board_address , topic_address):

	topic = Topic.objects.get(address = topic_address)

	comments = []
	for x in topic.comments.all():
		name = x.name
		name_len = 3*((len(name.encode("utf-8")) - len(name)) // 2) + len(name) # 中文字符占两个位置
		if name_len < 20: 
			name = name + (" " * (20-name_len))

		append = "\t\t--By %s | %2d楼" % (name , len(comments) + 1)
		append = append.replace(" " , "&nbsp")
		append = append.replace("\t" , 8*"&nbsp")
		comments.append((x.content , append))

	return render(request , "forum/topic.html" , {
		"topic" : topic,
		"comment_list" : comments,
	})


def new_topic(request , board_address):
	board = Board.objects.get(address = board_address)

	# only member can new a topic
	visitor = visitor_control.ask_visitor(request)
	if visitor is not None:
		if request.POST:
			name = request.POST.get('name')
			new_topic = Topic(board = board, name = name)
			new_topic.save()
	else:
		print("未登录")

	return http.HttpResponseRedirect("../" + board.address)

def new_comment(request , board_address , topic_address):
	topic = Topic.objects.get(address = topic_address)
	
	# only member can make comments
	visitor = visitor_control.ask_visitor(request)
	if visitor is not None:
		if request.POST:
			name = request.POST.get('name')
			content = request.POST.get('content')
			new_comment = FourmComment(topic = topic, content = content , name = name)
			new_comment.save()
	else:
		print("未登录")
	
	return http.HttpResponseRedirect("../" + topic.address)