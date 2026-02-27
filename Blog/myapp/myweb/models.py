from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
    b_img = models.FileField()
    b_title = models.TextField()
    b_heading = models.TextField()
    b_blog = models.TextField()
