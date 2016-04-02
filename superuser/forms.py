from django.conf import settings
import importlib
from superuser.models import *
from django import forms
from django.contrib.admin import widgets  
from django.forms import ModelForm
from .models import *

setlist = settings.SUPERUSER_FORM.split('.')
FormApp = importlib.import_module('.'.join(setlist[:-1]))
CForm = getattr(FormApp, setlist[-1])

setlist = settings.SUPERUSER_LFORM.split('.')
FormApp = importlib.import_module('.'.join(setlist[:-1]))
LForm = getattr(FormApp, setlist[-1])


setlist = settings.SUPERUSER_PRFORM.split('.')
FormApp = importlib.import_module('.'.join(setlist[:-1]))
PForm = getattr(FormApp, setlist[-1])

class FormTemp(CForm):
    pass

class LFormTemp(LForm):
    pass

class PRForm(PForm):
    pass
