
from django.contrib import admin
from django.urls import path, include
from base import views
urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('about', views.about, name='about'),
    path('conatact', views.contact, name='contact'),
    path('diabetes', views.diabetes, name='diabetes'),
    path('heartAttack', views.heartAttack, name='heartAttack'),
    path('lungCancer', views.lungCancer, name='lungCancer'),
    path('KidneyDisease', views.kidneyDisease, name='kidneyDisease'),
    path('hypertension', views.hypertension, name='hypertension'),
    path('parkinson', views.parkinson, name='parkinson'),
]
