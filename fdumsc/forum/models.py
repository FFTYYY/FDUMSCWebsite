from django.db import models
import django.utils.timezone as timezone
import os
import pdb

def cut_str(s):
	return s if len(s) < 20 else s[:17] + "..." 

class Board(models.Model):
	name = models.CharField(max_length = 20)
	address = models.CharField(max_length = 20 , default = "" , blank = True)
	friends = models.ManyToManyField("Board" , blank = True)

	def __str__(self):
		return self.name

	def save(self , *pargs , **kwargs):

		super().save(*pargs , **kwargs)
		
		for x in self.friends.all():
			if len(x.friends.filter(id = self.id)) == 0: # he don't have me in friends
				x.friends.add(self)
				x.save()
		super().save(*pargs , **kwargs)

		if not self.address:
			self.address = "forum_%d" % self.id

		return super().save(*pargs , **kwargs)

class Topic(models.Model):
	board = models.ForeignKey(Board , on_delete = models.CASCADE  , related_name = "topics")
	name = models.TextField(default = "")
	address = models.CharField(max_length = 20 , default = "" , blank = True)

	def __str__(self):
		return self.name

	def save(self , *pargs , **kwargs):
		if not self.address:
			super().save(*pargs , **kwargs)
			self.address = "topic_%d" % self.id
		return super().save(*pargs , **kwargs)


class FourmComment(models.Model):

	topic = models.ForeignKey(Topic , on_delete = models.CASCADE  , related_name = "comments")
	content = models.TextField(default = "")
	name = models.CharField(max_length = 20 , default = "")

	def save(self , *pargs , **kwargs):
		if not self.name:
			self.name = "匿名"
		return super().save(*pargs , **kwargs)

	def __str__(self):
		return cut_str(self.content)