from django.urls import path
from . import views

urlpatterns = [
       
       path('form/', views.UserFun, name = 'form'),
       path('success/', views.SuccessFun, name = 'success'),
]