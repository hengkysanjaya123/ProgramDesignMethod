from django.urls import path, include
from . import views

urlpatterns = [
    path('' ,views.home),
    path('traindata', views.traindata, name='traindata'),
    path('doattendance', views.doattendance, name='doattendance'),
    path('submit', views.submit)
]
