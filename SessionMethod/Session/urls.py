from django.urls import path
from . import views

urlpatterns = [
    path('c/', views.CheckCookie, name = 'check'),
    path('s/', views.SetCookie, name = 'set'),
    path('d/', views.DeleteCookie, name = 'delete'),
]
