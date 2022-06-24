from django.urls import path
from . import views

urlpatterns = [
    path('c/', views.CreatingCookies, name = 'creating'),
    path('g/', views.GettingCookies, name = 'getting'),
    path('d/', views.DeletingCookies, name = 'deleting')
]
