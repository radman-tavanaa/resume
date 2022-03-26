from tabnanny import verbose
from django.db import models
from datetime import datetime
from django.utils.translation import gettext_lazy as _

# Create your models here.

# /// RESUME ///
class  Work(models.Model):
    title     = models.CharField(max_length=150 , verbose_name=_('title'))
    sub_title = models.CharField(max_length=150 , verbose_name=_('sub title'))
    start     = models.DateTimeField(blank=True , null=True , verbose_name= _('start date'))
    end       = models.DateTimeField(default=datetime.today() , blank=True , null=True , verbose_name=_('end date'))
    custom_duration = models.CharField(max_length=120 , blank=True , verbose_name= _('custom duration '))
    details   = models.TextField(verbose_name= _('details'))

    class Meta:
        verbose_name = _('Work')
        verbose_name_plural = _('Works')

    def __str__(self):
        return self.title


class Educations(models.Model):
    title     = models.CharField(max_length=150 , verbose_name=_('title'))
    sub_title = models.CharField(max_length=150 , verbose_name=_('sub title'))
    start     = models.DateTimeField(blank=True , null=True , verbose_name= _('start date'))
    end       = models.DateTimeField(default=datetime.today() , blank=True , null=True , verbose_name=_('end date'))
    custom_duration = models.CharField(max_length=120 , blank=True , verbose_name= _('custom duration '))
    details   = models.TextField(verbose_name= _('details'))

    class Meta:
        verbose_name = _('education')
        verbose_name_plural = _('educations')


    def __str__(self):
        return self.title



# /// SERVICES ///
class services(models.Model):
     title = models.CharField(max_length=120)
     descriptins = models.TextField()

     def __str__(self):
         return self.title

     