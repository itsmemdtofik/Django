from django.shortcuts import render
from datetime import datetime, timedelta
def SetCookies(request):
    response = render(request, 'student/Setcookies.html')
    response.set_cookie('lname', 'khan', expires=datetime.utcnow() + timedelta(days=2))
    return response

def GetCookies(request):
    """name = request.COOKIES['name']
    name = request.COOKIES.get('name')"""
    name = request.COOKIES.get('name', "Guest")
    return render(request, 'student/Getcookies.html', {'name':name})

def DeleteCookies(request):
    response = render(request, 'student/Deletecookies.html')
    response.delete_cookie('name')
    return response