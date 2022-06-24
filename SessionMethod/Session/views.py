from email.policy import default
from django.shortcuts import render

def SetCookie(request):
    request.session.set_test_cookie()
    return render(request, 'Session/Setcookie.html')

def CheckCookie(request):
    request.session.test_cookie_worked()
    return render(request, 'Session/Checkcookie.html')

def DeleteCookie(request):
    request.session.delete_test_cookie()
    return render(request, 'Session/Deletecookie.html')
