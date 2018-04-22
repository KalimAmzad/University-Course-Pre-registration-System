from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^applying-courses/',views.applying_courses,name='applying_courses'),
    url(r'^teacher-assign/',views.teacher_assign,name='teacher_assign'),


]
