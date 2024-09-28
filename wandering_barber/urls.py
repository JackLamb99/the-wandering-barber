"""
URL configuration for wandering_barber project.

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
from django.urls import path, include
from .views import index, about, contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),  # Home page URL
    path('about/', about, name='about'),  # About page URL
    path('contact/', contact, name='contact'),  # Contact page URL
    path('', include('users.urls')),  # Links users app URLs
    path('', include('appointments.urls')),  # Links reviews app URLs
]
