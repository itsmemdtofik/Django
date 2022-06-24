from django.urls import path
from . import views

urlpatterns = [

    path('student/', views.StudentFun, name = 'student'),
    path('teacher/', views.TeacherFun, name = 'teacher'),
    path('success/', views.RegistrationSuccess, name = 'success')
]