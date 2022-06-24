from django.http import HttpResponse
from django.shortcuts import render

def SetPage(request):
    request.session['name'] = "Muhammad tofik"
    return render(request, 'bank/Setpage.html')

def CheckPage(request):
    name = request.session['name']
    return render(request, 'bank/Getpage.html', {'name' : name})
    

def DeletePage(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'bank/Deletepage.html')
