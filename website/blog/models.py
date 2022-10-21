from distutils.command.upload import upload
from statistics import mode
from turtle import title
from django.db import models

# Create your models here.
class Blogpost(models.Model):
    title = models.CharField(max_length=100,blank=True,null=True)
    content =models.TextField(max_length=5000,blank=True,null=True)
    created_on =models.DateTimeField(auto_now=False,auto_no_add=True)
    thumbnail =models.ImageField(upload_to="thumpnail/")
    author =models.CharField(max_length=50)