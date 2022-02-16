from django.contrib import admin
from django.urls import path
from EventsApp.views import *
urlpatterns = [
    path('',home,name='home'),
    path('userlogin/',userlogin,name='userlogin'),
    path('register/',register,name='register'),
    path('vieweventspage/',viewevents,name='viewevents'),
    path('logout/',logoutall,name='logouts'),
    path('eventenroll/<int:eveid>/',eventenrollact,name='eventenroll'),
    path('eventenrolled/',eventenrolled,name='eventenrolled'),
    path('studash/',studash,name='studdash'),
]