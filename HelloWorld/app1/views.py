from django.shortcuts import render
from django.http import HttpResponse

def HelloWorld(request):
	return HttpResponse('<h1 style = "text-align:center;" >HelloWorld</h1>')
