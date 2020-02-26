from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    # ex: /articles/
	path("", views.index, name="index"),
    # ex: /articles/5/
    path("<int:article_id>/", views.detail, name="detail"),
    # ex: /articles/search/
    path("search/", views.search, name="search"),
    # ex: /articles/5/commit_comment
    path("<int:article_id>/commit_comment/", views.commit_comment, name="commit_comment"),
    # ex: /articles/5/DoVote
    path("<int:article_id>/DoVote", views.DoVote, name="DoVote"),
]