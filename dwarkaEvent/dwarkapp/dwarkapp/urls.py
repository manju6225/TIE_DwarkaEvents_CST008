"""dwarkapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from . import views

urlpatterns = [
    path('Manju/', admin.site.urls),
    path('', views.home),
    path('base', views.home, name='base'),

    path('home/', views.home, name='home'),
    path('/base/', views.home, name='home'),
    path('price/checkout.html/saveform', views.dtabase, name="dtabase"),

    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('price/', views.price, name='price'),
    path('review/', views.review, name='review'),
    path('service/', views.service, name='service'),
    path('gallery/', views.gallery, name='gallery'),
    path('price/checkout.html/', views.checkout, name='checkout'),
    path('checkout/success/', views.checkout_success, name='checkout_success'),
]