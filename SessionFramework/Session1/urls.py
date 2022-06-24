from django.urls import path
from . import views

urlpatterns = [
    path('s/', views.SetSession, name = 'set' ),
    path('g/', views.GetSession, name = 'get'),
    path('d/', views.DelSession, name = 'delete'),
]
