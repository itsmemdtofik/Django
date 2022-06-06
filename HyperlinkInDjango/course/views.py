from django.shortcuts import render

def home(request):
	return render(request, 'course/Home.html')

def about(request):
	return render(request, 'course/About.html')

def contact(request):
	return render(request, 'course/Contact.html')

def signup(request):
	return render(request, 'course/Signup.html')
