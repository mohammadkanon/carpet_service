from django.db import models

# Create your models here.
class Blog(models.Model):
    blog_title = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateTimeField(default=None)
    blog_comment = models.CharField(max_length=20, null=True, blank=True)
    blog_description = models.TextField(blank=True, null=True)
    blog_button = models.CharField(max_length=15, null=True, blank=True)
    blog_img = models.ImageField(upload_to='blog', null=True, blank=True)