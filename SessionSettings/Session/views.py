from email.policy import default
from django.shortcuts import render

def SetCookie(request):
    request.session['name'] = 'Muhammad Tofik'
    return render(request, 'Session/Setcookie.html')

def CheckCookie(request):
    name = request.session['name']
    print(name)
    print(request.session.get_expiry_age())
    print(request.session.get_expiry_date())
    print(request.session.get_expire_at_browser_close())
    return render(request, 'Session/Checkcookie.html', {'name' : name})

def DeleteCookie(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'Session/Deletecookie.html')
