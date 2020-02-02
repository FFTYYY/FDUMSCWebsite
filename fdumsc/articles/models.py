from django.db import models
import django.utils.timezone as timezone
import os

class Article(models.Model):
	title = models.CharField(max_length = 20 , default = "" , blank = True)
	content = models.TextField (default = "" , blank = True)
	address = models.CharField (max_length = 20 , default = "" , blank = True , null = True)

	def __str__(self):
		return self.name

	def save(self , *pargs , **kwargs):

		if not self.address:
			super().save(*pargs , **kwargs) # get self.id
			self.address = "article_%d" % self.id

		return super().save(*pargs , **kwargs)

class Comment(models.Model):
	target = models.ForeignKey(Article , on_delete = models.CASCADE  , related_name = "Comment")
	content = models.TextField(default = "")
	name = models.CharField(max_length = 20 , default = "匿名")
