from django.urls import path
from . import views

app_name = __package__

urlpatterns = [
	path("signup/", views.sign_up) ,
	path("signin/", views.sign_in) ,
	path("signout/", views.sign_out) ,
	path("signin/signin_submit", views.sign_in_submit) ,
	path("signup/signup_submit", views.sign_up_submit) ,
]
