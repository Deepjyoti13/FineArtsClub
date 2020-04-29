from django.db import models

# Create your models here.
class Pen_Paper(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='penpaper')

    def __str__(self):
        return self.name


class Digital(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='digital')

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='team')
    position = models.CharField(max_length=20)
    start_year = models.IntegerField(null=True)
    end_year = models.IntegerField(null=True)
    current = models.BooleanField(default=False)
    facebook = models.URLField(max_length=50, null=True, blank=True)
    instagram = models.URLField(max_length=50, null=True, blank=True)
    github = models.URLField(max_length=50, null=True, blank=True)
    linkedin = models.URLField(max_length=50, null=True, blank=True)
    gmail = models.URLField(max_length=50, null=True, blank=True)
    twitter = models.URLField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

class Moment(models.Model):
    name = models.CharField(max_length=25)
    img = models.ImageField(upload_to='moments')

    def __str__(self):
        return self.name

class Notice(models.Model):
    title = models.CharField(max_length=50)
    img = models.ImageField(upload_to='notice')
    desc = models.TextField()
    link = models.URLField(max_length=100)
    current = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
