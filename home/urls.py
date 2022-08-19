from operator import concat
from django.contrib import admin
from django.urls import path,include
from .views import contact, index,about,maison,service

urlpatterns = [
    path("",index, name="home"),
    path("about/",about, name="about"),
    path("contact/",contact, name="contact"),
    path("maison/",maison, name="maison"),
    path("services/",service, name="service"),
]
