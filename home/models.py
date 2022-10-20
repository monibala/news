from django.db import models

# Create your models here.

class slider(models.Model):
    image = models.ImageField()
    date = models.DateField()
    title = models.CharField(max_length=300)
    desc= models.TextField()


class news_trend(models.Model):
    head1 = models.CharField(max_length=100)
    head2 = models.CharField(max_length=100)
    head3 = models.CharField(max_length=100)
    image = models.ImageField()
    date = models.DateField()
    writer_name = models.CharField(max_length=100)
    writer_image= models.ImageField()
    title = models.CharField(max_length=300)
class gallery(models.Model):
    image = models.ImageField()
    desc = models.TextField()

class popular(models.Model):
    image = models.ImageField()
    title = models.TextField()
    desc = models.TextField()
class features(models.Model):
    desc = models.TextField()
    date = models.DateField(null=True)
