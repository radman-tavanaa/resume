from modeltranslation.translator import translator, TranslationOptions
from .models import *


class WorkTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'sub_title',
        'start',
        'end',
        'custom_duration',
        'details',
    )

translator.register(Work , WorkTranslationOptions)

class EducationsTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'sub_title',
        'start',
        'end',
        'custom_duration',
        'details',
    )

translator.register(Educations , EducationsTranslationOptions)