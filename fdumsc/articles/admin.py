from django.contrib import admin
from .models import Article, Comment

# Register your models here.

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    # add list at the admin site
    list_display = ('title', 'author', 'Type', 'pub_date')
    # add search option at the admin site
    search_fields = ['title']
    # classify the infomation of articles
    fieldsets = [
        ('Basic Information', {'fields': ['title', 'author', 'Type', 'pub_date']}),
        ('Content information', {'fields': ['content'], 'classes': ['collapse']}),
    ]
    # add choices at the bottom
    inlines = [CommentInline]

# register Article
admin.site.register(Article, ArticleAdmin)
