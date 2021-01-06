"""studentModal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from .views import GeneratePDF
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='master'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_, name='login'),
    path('logout/', views.logout_, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('student-dashboard', views.student_dashboard, name='student_dashboard'),
    path('student/', include('Student.urls')),
    path('student/', include('Marks.urls')),
    path('courses/', views.courses, name='courses'),
    path('after-login/', views.after_login, name='after_login'),
    path('htm-pdf/',GeneratePDF.as_view(), name= 'htm_pdf')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
