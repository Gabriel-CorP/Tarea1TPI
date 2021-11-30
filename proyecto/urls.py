"""proyecto URL Configuration

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
from django.urls import path
from proyectoApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index,name='index'),
    path('consola/', views.pcli,name='consola'),
    path('arrays/', views.arrays,name='arrays'),
    path('estructura_datos/', views.estructuraDatos,name='estructura_datos'),
    path('estructura_datos/arraylist/', views.arraylist,name='arraylist'),
    path('estructura_datos/queue/', views.queue,name='queue'),
    path('estructura_datos/stack/', views.stack,name='stack'),
    path('estructura_datos/sortedlist/', views.sortedlist,name='sortedlist'),
]
