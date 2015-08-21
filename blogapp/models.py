from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class userinfo(models.Model):
	username = models.CharField(max_length=20,unique=True)
	password = models.CharField(max_length=20)
	email = models.EmailField()
	def __unicode__(self):
		return self.username



class article(models.Model):
        title = models.CharField(max_length=150,unique=True)
        category_option = (
                ('Linux','Linux Blog'),
                ('Database','Database Blog'),
                ('Virtualization','Virtualization Blog'),
                ('Cluster','Cluster Blog'),
                ('Monitor','Monitor Blog'),
                ('Automation','Automation Blog'),
                ('Python','Python Blog'),
                ('Security','Security Blog'),
	)
        category = models.CharField(max_length=50,choices=category_option)
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


