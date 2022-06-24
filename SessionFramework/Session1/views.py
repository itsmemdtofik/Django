from django.shortcuts import render

def SetSession(request):
    request.session['name'] = 'Muhammad Tofik'
    request.session.set_expiry(10)
    return render(request, 'Session1/Setsession.html')

def GetSession(request):
    name = request.session['name']
    print(request.session.get_expiry_age())
    print(request.session.get_expiry_date())
    print(request.session.get_expire_at_browser_close())
    return render(request, 'Session1/Getsession.html', {'name': name})

def DelSession(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'Session1/Deletesession.html')
