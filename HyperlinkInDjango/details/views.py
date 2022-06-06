from django.shortcuts import render

def contact(request):
	return render(request, 'details/Contact.html')

def courseinfo(request):
	return render(request, 'details/CourseInfo.html', {'cr':'/courseinfo'})
