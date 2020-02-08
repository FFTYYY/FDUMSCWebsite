from django.db import models
import time
from .utils.cookie_control import *
import django.utils.timezone as timezone

class Visitor(models.Model):
	name = models.CharField(max_length = 200)
	password = models.CharField(max_length = 200 , blank = True)
	cookie_value = models.CharField(max_length = 200 , default = "")
	signup_time = models.DateTimeField(default = timezone.now)


	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		if self.cookie_value == "":
			self.cookie_value = make_cookie_value()
		return super().save(*args, **kwargs)
