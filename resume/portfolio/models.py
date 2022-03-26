from django.db import models
from datetime import datetime
# Create your models here.

class Category(models.Model):
    
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Projects(models.Model):
    category     = models.ForeignKey(Category, on_delete=models.DO_NOTHING , null=True)
    name         = models.CharField(max_length=120)
    client       = models.CharField(max_length=120 , blank=True)
    project_date = models.DateTimeField(blank=True)
    project_url  = models.URLField(max_length=200)
    title        = models.CharField(max_length=200)
    body         = models.TextField()
    photo_main   = models.ImageField(upload_to='project/photo/%Y%M%d/')

    def __str__(self):
        return self.name

class ProjectImage(models.Model):
    pass
    