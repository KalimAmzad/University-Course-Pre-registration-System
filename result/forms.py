from django import forms
from django.contrib.auth.models import User

class ResultForm(forms.Form):
    course_code = forms.CharField(max_length=64)
    section = forms.CharField(max_length=64)
    result_file = forms.FileField()


