"""
URL configuration for crud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from posts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    #Read(all)
    path('posts/<int:id>/', views.detail),
    #Read(1)
    #posts/1/
    #posts/10/
    #posts/123/ 얘네들 다 내가 처리할테니까 걱정들 붙들어매쇼잉
    path('posts/new/', views.new),
    path('posts/create/', views.create),
    #Create
]
