from django.shortcuts import render

def home(request):
	return render(request, 'Base/home.html')


def about(request):
	return render(request, 'Base/about.html')

def child(request):
	return render(request, 'Base/child.html')
