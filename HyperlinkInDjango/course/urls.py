from django.urls import path
from . import views

urlpatterns = [
   
   path('home/', views.home, name = 'homeus'),
   path('about/', views.about, name = 'aboutus'),
   path('contact/', views.contact, name = 'contactus'),
   path('signup/', views.signup, name = 'signus'),

]