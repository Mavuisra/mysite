from distutils.command.upload import upload
import email
from email.mime import image
from unittest.util import _MAX_LENGTH
from django.db import models

class createBlog(models.Model):
    title = models.CharField(max_length=255)
    slog = models.SlugField()
    intro = models.TextField()
    body = models.TextField(default = 'boby') 
    image = models.ImageField(upload_to='media')
    date_added = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    class Meta():
        ordering = ['date_added']
class comments(models.Model):
    post = models.ForeignKey(createBlog, related_name = 'comments', on_delete = models.CASCADE)
    email = models.EmailField()
    body = models.TextField()
    name = models.CharField(max_length= 255, default = 'inconnu')
    date_added = models.DateTimeField(auto_now=True)
    class Meta():
        ordering = ['date_added']
