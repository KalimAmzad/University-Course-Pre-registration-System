from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^pre-registration/', views.pre_registration, name='pre_registration'),
    url(r'^taken_courses/',views.taken_courses,name='taken_courses')

]
