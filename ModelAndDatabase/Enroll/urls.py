from django.urls import path
from . import views

urlpatterns = [
   
   path('khaini/', views.chaini_khaini, name = 'Chaini_Khaini'),
   
]