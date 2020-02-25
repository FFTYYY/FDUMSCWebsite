from django.db import models
from mdeditor.fields import MDTextField

# Create your models here.

class Article(models.Model):

    # define the type of articles
    class ArticleType(models.IntegerChoices):
        LEARNING = 1
        INTERVIEW = 2
        EXERCISE = 3
    
    # the infomation of an article
    title = models.CharField(max_length=20 , default="") 
    author = models.CharField(max_length=20 , default="匿名")
    pub_date = models.DateField()  
    Type = models.IntegerField(choices=ArticleType.choices)    # the type of an article
    content = MDTextField()                                    # using markdown
    # votes = models.ManyToManyField("authorization.Visitor", on_delete=models.CASCADE)

    # show title when showing
    def __str__(self):
        return self.title
    

class Comment(models.Model):
    
    # the information of a comment
    target = models.ForeignKey(Article , on_delete=models.CASCADE)  # the article which the comment is related to
    pub_date = models.DateField()
    content = models.TextField(default="")
    
    # show id when showing
    def __str__(self):
        return str(self.id)