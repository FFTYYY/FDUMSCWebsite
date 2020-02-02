from django.contrib import admin
from .models import *
from django.utils.html import format_html

class BoardAdmin(admin.ModelAdmin):
	filter_horizontal = ["friends"]

admin.site.register(Board , BoardAdmin)
admin.site.register(Topic)
admin.site.register(FourmComment)