from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^upload-result/', views.upload_result, name='upload_result'),
    

]
