from django.urls import path
from . import views

urlpatterns = [
path('courseone/', views.course_one),
path('coursetwo/', views.course_two),

]