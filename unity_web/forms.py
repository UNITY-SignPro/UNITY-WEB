from django import forms
from .models import passage

class PsgForm(forms.Form) :
    content = forms.IntegerField()
    