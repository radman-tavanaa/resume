from modeltranslation.translator import translator, TranslationOptions
from .models import *

# translate about models
class AboutTranslationOptions(TranslationOptions):
    fields = (
        'degree',
        'expertise',
        'details',
        'city',
        'gender',
        'explanation',
        'age',
    )

translator.register(About , AboutTranslationOptions)

# //// ABOUT TRANSLATION ////
class Skill_IntroTranslationOptions(TranslationOptions):
    fields = (
        'intro',
    )

translator.register(Skill_Intro , Skill_IntroTranslationOptions)

# //// FACTS TRANSLATION ////
class FACTSTranslationOptions(TranslationOptions):
    fields = (
        'intro',
       
    )

translator.register(FACTS , FACTSTranslationOptions)

#translate testimonials
class T_IntroTranslationOptions(TranslationOptions):
    fields = (
        'intro',
    )

translator.register(T_Intro , T_IntroTranslationOptions)

class testimonialsTranslationOptions(TranslationOptions):
    fields = (
        'person_name',
        'person_job',
        'comments',
    )

translator.register(testimonials , testimonialsTranslationOptions)