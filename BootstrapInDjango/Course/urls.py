from django.urls import path
from . import views

urlpatterns = [
    path('courseinfo/', views.courseinfo, name = 'Course'),
]