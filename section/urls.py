from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^check-section/', views.check_section, name='check_section'),
    url(r'^merge-section/', views.merge_section, name='merge_section'),
    

]
