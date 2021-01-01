from django.urls import path
from .import views     #import views from same directory.[todolist]

urlpatterns = [
    path('', views.index,name='index')
]