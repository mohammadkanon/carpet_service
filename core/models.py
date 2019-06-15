from django.db import models

# Create your models here.
class SliderTop(models.Model):
    slider_img = models.ImageField(upload_to='random_img', null=True, blank=True)
    slider_caption = models.CharField(max_length=20, null=True, blank=True)
    slider_description = models.CharField(max_length=30, null=True, blank=True)
    slider_description2 = models.CharField(max_length=30, null=True, blank=True)
    slider_button = models.CharField(max_length=15, null=True, blank=True)

class FstWall(models.Model):
    fst_img = models.ImageField(upload_to='f_wall')
    fst_content = models.CharField(max_length=100, null=True, blank=True)
    fst_description = models.TextField(null=True, blank=True)

class Work(models.Model):
    work_img = models.ImageField(upload_to='work', null=True, blank=True)
    work_title = models.CharField(max_length=20, blank=True, null=True)

class PeopleSay(models.Model):
    people_say = models.CharField(max_length=250, null=True, blank=True)

class PriceSection(models.Model):
    price = models.CharField(max_length=10, null=True, blank=True)
    area = models.CharField(max_length=10, null=True, blank=True)
    living = models.CharField(max_length=10, null=True, blank=True)
    content = models.TextField(blank=True, null=True)
    button = models.CharField(max_length=50, null=True, blank=True)

class Blog(models.Model):
    foot_pth = models.ImageField(upload_to='foot', null=True, blank=True)
    feature = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateTimeField(default=None)
    comment = models.CharField(max_length=10, null=True, blank=True)


