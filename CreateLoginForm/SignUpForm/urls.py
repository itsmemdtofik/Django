from django.urls import path
from . import views

urlpatterns = [

    path('signup/', views.Signup, name = 'signup'),
    path('login/', views.Login, name = 'login'),
    path('profile/', views.UserProfile, name = 'profile'),
    path('logout/', views.Logout, name = 'logout'),
]