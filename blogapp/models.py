from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class userinfo(models.Model):
	username = models.CharField(max_length=20,unique=True)
	password = models.CharField(max_length=20)
	email = models.EmailField()
	def __unicode__(self):
		return self.username




class categoryName(models.Model):
	category_name = models.CharField(max_length=20,unique=True)
	def __unicode__(self):
		return self.category_name

class article(models.Model):
        title = models.CharField(max_length=150,unique=True)
        category = models.ForeignKey(categoryName)
        content = models.TextField()
        view_count = models.IntegerField(default=0)
        comment_count = models.IntegerField(default=0)
        ranking = models.IntegerField(default=1001)
        author = models.ForeignKey(User)
        publish_date = models.DateField()
        modify_date = models.DateField()
	archives_date = models.CharField(max_length=10)
        def __unicode__(self):
                return self.title


