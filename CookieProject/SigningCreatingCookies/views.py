from email.policy import default
from urllib import response
from django.shortcuts import render
from datetime import datetime, timedelta

def CreatingCookies(request):
    response = render(request, 'SigningCreatingCookies/Setcookies.html')
    response.set_signed_cookie('name', 'Muhammad', salt= 'khan', expires = datetime.utcnow() + timedelta(days=2))
    return response

def GettingCookies(request):
    name = request.get_signed_cookie('name', default = 'Guest', salt = 'khan')
    return render(request, 'SigningCreatingCookies/Getcookies.html', {'name':name})

def DeletingCookies(request):
    response = render(request, "SigningCreatingCookies/Deletecookies.html")
    response.delete_cookie('name')
    return response

