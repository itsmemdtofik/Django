from django.urls import path
from . import views

urlpatterns = [
    path('<int:my_id>/', views.clickResponse, name = 'details'),
    path('<int:my_id>/<int:my_subid>/', views.AnotherClickResponse, name = 'subDetails'),
]


