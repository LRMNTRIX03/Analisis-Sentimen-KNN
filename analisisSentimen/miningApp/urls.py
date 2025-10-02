from django.urls import path

from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('input/', views.inputData, name='input.index'),
    path('preprocessing/', views.Preprocessing, name='preprocessing.index'),
]