"""
URL configuration for library_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from books import views
from .views import book_list, book_create, book_update, book_delete

urlpatterns = [
    path('', views.index),
    path('', book_list, name='book_list'),


    path("admin/", admin.site.urls),
    #path('books/', include('books.urls')),
    #path('new/', book_create, name='book_list'),
    path('new', book_create, name = 'book_create'),
    path('edit/<int:pk>/', book_update, name = 'book_update'),
    path('delete/<int: pk>/', book_delete, name = 'book_delete'),
]
