from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import StudentProfile,TeacherProfile


class LoginForm(forms.Form):
    username = forms.CharField(label='Id')
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label="Id")
    mobile = forms.IntegerField()
    email = forms.EmailField()
    sex = forms.CharField()
    semester = forms.CharField()
    section = forms.CharField()
    address = forms.CharField()
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class StudentProfileEditForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ('mobile', 'photo','address')

class TeacherProfileEditForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ('mobile', 'photo','address')
