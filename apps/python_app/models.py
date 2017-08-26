from __future__ import unicode_literals
from django.db import models
# Create your models here.

class User(models.Model):
	name = models.CharField(max_length=255)
	alias = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)


class Quote(models.Model):
	message = models.TextField(default=None)
	quote_by = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	quotes = models.ManyToManyField(User, related_name = "fav_quotes")
	uploader = models.ForeignKey(User, blank= True, null=True, related_name = "upload_quotes")


