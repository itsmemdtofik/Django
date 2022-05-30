from django.urls import path
from . import views


urlpatterns = [
    path('tofik/', views.studentinfo),
    path('tofik/khan/', views.studentComment),
    path('tofik/khan/geek/', views.myGeekForm),
]