from django.db import models
from mdeditor.fields import MDTextField
from enum import IntEnum, unique

# Create your models here.
@unique
class ArticleType(IntEnum):
    LEARNING = 1
    INTERVIEW = 2
    EXERCISE = 3


class Article(models.Model):
    # the title of an article
    title = models.CharField(max_length=20 , default="")
    # the author of an article
    author = models.CharField(max_length=20 , default="匿名")
    # the published date of an article
    pub_date = models.DateField()
    # the type of an article
    Type = models.IntegerField(default=0)
    # the content of an article
    content = MDTextField()   # use markdown

    # show title when showing
    def __str__(self):
        return self.title
    

class Comment(models.Model):
    # the article which the comment is related to
    target = models.ForeignKey(Article , on_delete=models.CASCADE)
    # the date of a comment
    pub_date = models.DateField()
    # the content of a comment
    content = models.TextField(default="")
    
    # show id when showing
    def __str__(self):
        return str(self.id)