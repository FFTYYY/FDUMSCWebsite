from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
	path("" , views.index),
	path("<str:article_address>/submit_comment" , views.upload_comment) , 
	path("<str:article_address>/" , views.get_article) ,

]