from django.http import HttpResponse
from django.shortcuts import render

def SetPage(request):
    request.session['name'] = "Muhammad tofik"
    return render(request, 'bank/Setpage.html')

def CheckPage(request):
    if 'name' in request.session:
        name = request.session['name']
        request.session.modified = True
        return render(request, 'bank/Getpage.html', {'name' : name})
    else:
        return HttpResponse('<center><h1>Your session has been expired. </h1></center>')

def DeletePage(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request, 'bank/Deletepage.html')
