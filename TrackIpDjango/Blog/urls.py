from django.urls import path
from . import views

urlpatterns = [
      
      path('', views.home, name = 'home'),
      path('about/', views.about, name = 'about'),
      path('dashboard/', views.dashboard, name = 'dashboard'),
      path('contact/', views.contact, name = 'contact'),
      path('logout/', views.UserLogout, name = 'logout'),
      path('signup/', views.UserSignup, name = 'signup'),
      path('login/', views.UserLogin, name = 'login'),
      path('add/', views.AddPost, name = 'add'),
      path('update/<int:id>/', views.UpdatePost, name = 'update'),
      path('delete/<int:id>/', views.DeletePost, name = 'delete'),
]