from django.urls import path
from . import views

urlpatterns = [

    path('form/', views.myDjangoForm, name = 'form'),
    path('success/', views.RegistrationSuccess, name = 'Success')
]