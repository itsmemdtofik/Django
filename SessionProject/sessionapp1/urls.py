from django.urls import path
from . import views

urlpatterns = [

    path('sessionConnection/', views.sessionConnection, name="connection"),
    path('sessionLogin/', views.sessionLogin, name="Login Page"),
    path('sessionFormView/', views.sessionFormView, name="Form View"),
    path('sessionLogout/', views.sessionLogout, name="Form Views"),
]
