from tabnanny import verbose
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime
from django.utils.translation import gettext_lazy as _

# /// ABOUT ///

class About(models.Model):
    degree      = models.CharField(max_length=120 , verbose_name= _('Degree'))
    expertise   = models.CharField(max_length=120 , verbose_name=_('Expertise'))
    details     = models.CharField(max_length=120 , verbose_name= _('Details'))
    city        = models.CharField(max_length=120 , verbose_name=_('City'))
    email       = models.CharField(max_length=120 , blank=True , verbose_name=_('Email'))
    age         = models.IntegerField(default=15 , verbose_name=_('Age'))
    gender      = models.CharField(max_length=15 , blank=True , verbose_name=_('Gender'))
    image       = models.ImageField(upload_to='photos/%Y%M%d/' , null=True , verbose_name=_('Image')) 
    explanation = models.TextField(null=True , verbose_name=_('Explanation'))
    
    class Meta:
        verbose_name = _("About")
        verbose_name_plural = _("Abouts")
        

    def __str__(self):
       return self.email

# /// MY SKILLS ///

class Skill_Intro(models.Model):
    intro = models.TextField(blank=True , verbose_name=_('skill introduction'))

    class Meta:
        verbose_name = _('skill_Intro')
        verbose_name_plural = _('skill_Intros')


class CodingSkills(models.Model):
    skill_name   = models.CharField(max_length=40 , verbose_name=_('skill'))
    skill_rate   = models.IntegerField(default=1 , validators=[MinValueValidator(0),MaxValueValidator(100)] , verbose_name=_('rate'))

    def __str__(self):
        return self.skill_name

class CodingSkills2(models.Model):
    skill_name = models.CharField(max_length=40 , verbose_name=_('skill'))
    skill_rate = models.IntegerField(default=1 , verbose_name=_('rate') ,validators=[MinValueValidator(0),MaxValueValidator(100)])

    def __str__(self):
        return self.skill_name



# /// FACTS ///

class FACTS(models.Model):
    intro = models.TextField(blank=True)
    client = models.IntegerField(default=1 , verbose_name=_('Clients') )
    projects = models.IntegerField(default=1 , verbose_name=_("Projects"))
    hour_of_support = models.IntegerField(default=1 , verbose_name=_("Hours Of Support"))
    experience = models.IntegerField(default=1 , verbose_name=_("Year Of Experience"))

    class Meta:
        verbose_name = _('Fact')
        verbose_name_plural = _('Facts')

# /// testimonials ///

class T_Intro(models.Model):
    intro = models.TextField(blank=True , verbose_name=_('introduction'))

    class Meta:
        verbose_name = _('T_Intro')
        verbose_name_plural = _('T_Intros')

class testimonials(models.Model):
    person_name  = models.CharField(max_length=120 , verbose_name=_('Person Name'))
    person_job   = models.CharField(max_length=120 , verbose_name=_('Person job'))
    comments     = models.TextField(verbose_name=_('Comments'))
    image        = models.ImageField(upload_to='testimonials/photo%Y%M%d/' , verbose_name=_('Image'))

    class Meta:
        verbose_name = _('testimonial')
        verbose_name_plural = _('testimonials')

    def __str__(self):
        return self.person_name




#///////////////////////////////////////////////



# //// contact us 

''''
class ContactMe(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subjects = models.CharField(max_length=100)
    messages = models.TextField()

    def __str__(self):
        return self.name

class info(models.Model):
    location = models.TextField()
    email = models.EmailField()
    number = models.IntegerField()

    def __str__(self):
        return self.email
'''

    





    