from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register([About , CodingSkills , CodingSkills2 , testimonials])
admin.site.register([T_Intro , FACTS , Skill_Intro])
