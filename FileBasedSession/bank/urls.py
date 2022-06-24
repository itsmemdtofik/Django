from django.urls import path
from . import views

urlpatterns = [
    path('s/', views.SetPage, name = 'set' ),
    path('c/', views.CheckPage, name = 'check'),
    path('d/', views.DeletePage, name = 'delete'),
]
