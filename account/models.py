from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class StudentProfile(models.Model):
    gender = (
    ('M', 'Male'),
    ('F', 'Female'),
)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    mobile = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=256,blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    sex = models.CharField(max_length=10,choices=gender,default='Male',blank=True,null= True)
    semester = models.CharField(max_length=32)
    section = models.CharField(max_length=3)
    
    def __str__(self):
        return self.user.username


class TeacherProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,)
    mobile = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=256,blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    
    def __str__(self):
        return self.user.username
