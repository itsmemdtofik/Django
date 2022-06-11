from django.shortcuts import render
from Enroll.models import Student

def chaini_khaini(request):
	chaini = Student.objects.all()
	return render(request, 'Enroll/chaini.html', {'khaini': chaini})
