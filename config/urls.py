"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
<<<<<<< HEAD
from pybo.views import base_view

urlpatterns = [
    path("", base_view.index, name='index'),
    path("admin/", admin.site.urls),
    path('pybo/', include('pybo.urls')),
    path('common/', include('common.urls'))
=======
from pybo import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('pybo/',include('pybo.urls')),
>>>>>>> f0cf70c187a02ef13c7821c4c612dbff267fc274
]
