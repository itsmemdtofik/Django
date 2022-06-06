from django.urls import path
from . import views

urlpatterns = [
path('feesone/', views.fees_one),
path('feestwo/', views.fees_two),
path('info/', views.information),

]