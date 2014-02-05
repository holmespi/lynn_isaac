from django.db import models
from tinymce.models import HTMLField

# Create your models here.



class Post(models.Model):
	title = models.CharField(max_length=128, unique=True)
	date = models.DateField(auto_now=True)
	story = HTMLField()

	def __unicode__(self):
		return self.title
