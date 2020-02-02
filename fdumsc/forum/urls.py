from django.urls import path
from . import views

app_name = __package__

urlpatterns = [
	path("", views.index) ,
	path("<str:board_address>/" , views.get_board) ,
	path("<str:board_address>/newtopic_submit" , views.new_topic) , 
	path("<str:board_address>/<str:topic_address>/" , views.get_topic) ,
	path("<str:board_address>/<str:topic_address>/newcomment_submit" , views.new_comment) ,
]
