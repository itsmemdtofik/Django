from email.policy import default
from django.shortcuts import render

def SetSession(request):
    request.session['name'] = 'Muhammad'
    request.session['lname'] = 'Tofik'
    return render(request, 'Session/Setsession.html')

def GetSession(request):
    name = request.session.get('name')
    lname = request.session.get('lname')
    keys = request.session.keys()
    items = request.session.items()
    age = request.session.setdefault('age', '26')
    return render(request, 'Session/Getsession.html', {'name':name, 'lname':lname, 'key':keys, 'items':items, 'age':age})

def DelSession(request):
    #request.session.flush()
    if 'name' in request.session:
        del request.session['name']
    return render(request, 'Session/Deletesession.html')
