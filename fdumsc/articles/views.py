import markdown
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from .models import Article, Comment, ArticleType

# Create your views here.

# the index view of articles
# todo: list articles'titles according to their types
def index(request):
    learning_list = Article.objects.filter(Type=ArticleType.LEARNING).order_by('pub_date').values('id', 'title')
    inerview_list = Article.objects.filter(Type=ArticleType.INTERVIEW).order_by('pub_date').values('id', 'title')
    exercise_list = Article.objects.filter(Type=ArticleType.EXERCISE).order_by('pub_date').values('id', 'title')
    context = {'learning_list':learning_list, 'interview_list':inerview_list, 'exercise_list':exercise_list}
    return render(request, 'articles/index.html', context)


# the detail of an article
# todo: show the content and comments of an article
# and deal with the ewquest to add a new comment
def detail(request, article_id):
    # get the article
    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404("This article does not exist.")
    # add a new comment if needed
    if request.POST:
        comment_content = request.POST.get('comment_content')
        if comment_content != "":
            new_comment = Comment(target=article, pub_date=timezone.now().date(), content=comment_content)
            new_comment.save()
    # get the comments
    comments_list = Comment.objects.filter(target=article)
    # modify the article from markdown to html
    article.content = markdown.markdown(article.content.replace('\r\n', '  \n'), extensions=[
            'markdown.extensions.extra',    # 包含缩写、表格等常用扩展
            'markdown.extensions.codehilite',    # 语法高亮拓展
            'markdown.extensions.toc'], safe_mode=True, enable_attributes=False    #自动生成目录
        )
    context = {'article':article, 'comments_list':comments_list}
    return render(request, 'articles/detail.html', context)


# search articles according to the given keywords
def search_articles(request):
    if request.POST:
        keywords = request.POST.get('keywords')
        articles_list = Article.objects.filter(title__icontains=keywords).order_by('title').values('id', 'title')
        context = {'articles_list':articles_list}
        return render(request, 'articles/search.html', context)

