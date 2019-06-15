from django.db import models

# Create your models here.
class SndWall(models.Model):
    snd_img = models.ImageField(upload_to='f_wall')
    snd_content = models.CharField(max_length=100, null=True, blank=True)
    snd_description = models.TextField(null=True, blank=True)