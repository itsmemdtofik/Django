from django.urls import path
from . import views

urlpatterns = [
   
   path('contact/', views.contact, name = 'contactus'),
   path('courseinfo/', views.courseinfo, name = 'courseus'),
   

]