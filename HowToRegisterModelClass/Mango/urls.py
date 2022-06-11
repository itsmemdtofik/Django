from django.urls import path
from . import views

urlpatterns = [

  path('good/', views.MangoOrange, name = 'Chaini_Khaini'),
]