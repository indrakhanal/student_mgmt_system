from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('student-info/', views.student_info, name='student_info'),
    path('news/', views.news, name='news'),
    # path('show_news/', views.showNews, name='show_news')
]
