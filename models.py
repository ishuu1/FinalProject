from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=1000)
    body = models.TextField(max_length=2000)
    slug = models.SlugField(max_length= 255)
    image = models.ImageField(upload_to='blog')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now= True)

