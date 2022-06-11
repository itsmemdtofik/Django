from django.urls import path, register_converter
from . import views, converters

register_converter(converters.CustomePathConverter, 'tttt')

urlpatterns = [
    path('student/<tttt:saal>/', views.home, name = 'details'),
]


