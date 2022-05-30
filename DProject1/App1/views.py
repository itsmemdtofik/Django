from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	return HttpResponse("<h1 style = 'text-align:center;'>Hello Django </h1>")

def Profile(request):
    return render(request, 'ProfilePage.html', {'link' : 'http://127.0.0.1:8000/'})

def Calculator(request):
    return render(request, 'Index.html')