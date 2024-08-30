from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   path('',views.homepage,name='homepage'),
   path('kannur',views.kannur,name='kannur'),
   path('mission',views.mission,name='mission'),
   path('curry',views.curry,name='curry'),
]
