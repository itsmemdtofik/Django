from django.shortcuts import render
from Mango.models import Student

def MangoOrange(request):
	good = Student.objects.all()
	return render(request, 'Mango/good.html', {'very_good': good})
