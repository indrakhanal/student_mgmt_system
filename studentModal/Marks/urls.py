from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('marks-info/', views.search_marks, name='marks_info'),
    path('first-sem/', views.first_sem, name='first_sem'),
    path('second-sem/', views.second_sem, name='second_sem'),
]