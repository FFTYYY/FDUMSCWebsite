import markdown
import datetime
import json
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import Article, Comment, Vote
from authorization.utils import visitor_control

# Create your views here.

# the index view of articles
# todo: list articles'titles respectively according to their types
def index(request):
    learning_list = Article.objects.filter(Type=Article.ArticleType.LEARNING).order_by('pub_date').values('id', 'title')
    inerview_list = Article.objects.filter(Type=Article.ArticleType.INTERVIEW).order_by('pub_date').values('id', 'title')
    exercise_list = Article.objects.filter(Type=Article.ArticleType.EXERCISE).order_by('pub_date').values('id', 'title')
    context = {'learning_list':learning_list, 'interview_list':inerview_list, 'exercise_list':exercise_list}
    return render(request, 'articles/pindex.html', context)


# the detail of an article
# todo: 1) show the content and comments of an article
#       2) deal with the request to add a new comment
def detail(request, article_id):
    # get the article
    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404("This article does not exist.")
    # get the vote status
    visitor = visitor_control.ask_visitor(request)
    if visitor is None:
        IsVoting = False
    else:
        try:
            Vote.objects.get(article=article, visitor=visitor)
            IsVoting = True
        except Vote.DoesNotExist:
            IsVoting = False
    # get the comments list 
    comments_list = Comment.objects.filter(target=article)
    # modify the content from markdown to html
    article.content = markdown.markdown(article.content.replace('\r\n', '  \n'), extensions=[
            'markdown.extensions.extra',                                           # 包含缩写、表格等常用扩展
            'markdown.extensions.codehilite',                                      # 语法高亮拓展
            'markdown.extensions.toc'], safe_mode=True, enable_attributes=False    # 自动生成目录
        )
    # conduct the context
    context = {'article':article, 'IsVoting':IsVoting, 'comments_list':comments_list}
    return render(request, 'articles/pdetail.html', context)


# search articles
# todo: search articles with given keywords
def search(request):
    if request.POST:
        keywords = request.POST.get('keywords')
        articles_list = Article.objects.filter(title__icontains=keywords).order_by('title').values('id', 'title')
        context = {'articles_list':articles_list}
        return render(request, 'articles/psearch.html', context)


# commit a comment
# todo: 1) add a new comment
#       2) refresh the detail view
def commit_comment(request, article_id):
    # add a new comment if needed
    if request.POST:
        try:
            article = Article.objects.get(pk=article_id)
        except Article.DoesNotExist:
            raise Http404("This article does not exist.")
        comment_content = request.POST.get('comment_content')
        if comment_content != "":
            Comment.objects.create(target=article, pub_date=datetime.date.today(), content=comment_content)
    # redirect to the detail view
    return redirect(reverse('articles:detail', args=[article_id]))


# vote for an article
# todo: 1) commit or cancel a vote
#       2) update the votecnt of this article
#       3) refresh the detail view
def DoVote(request, article_id):
    # get the article
    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404("This article does not exist.")
    # commit or cancel a vote
    visitor = visitor_control.ask_visitor(request)
    if visitor is not None:
        try:
            vote = Vote.objects.get(article=article, visitor=visitor)
            vote.delete()
        except Vote.DoesNotExist:
            Vote.objects.create(article=article, visitor=visitor)
    else:
        print("未登录")
    # update the votecnt
    votecnt = Vote.objects.filter(article=article).count()
    article.votecnt = votecnt
    article.save()
    # redirect to the detail view
    # return redirect(reverse('articles:detail', args=[article_id]))
    # refresh the detail view
    return HttpResponse(json.dumps("ok"))


