from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from mapwebapp import views
# from mapwebapp import web_views
urlpatterns = [
    url('checking', views.checking),
    url('index03',views.index03),
    url('check',views.check),
    url('getAllData',views.getAllData),
    url('getLastData',views.getLastData)
]