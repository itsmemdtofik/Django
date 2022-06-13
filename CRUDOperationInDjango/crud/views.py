from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentForm
from .models import Student

#This is for inserting and displaying records
def InsertAndDisplay(request):
	if request.method == 'POST':
		form = StudentForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			myRecords = Student(name = name, email = email, password = password)
			myRecords.save()
			form = StudentForm()		
	else:
		form = StudentForm()
	student = Student.objects.all()
	return render(request, 'crud/InsertAndDisplay.html', {'form':form,'student':student})


#This is for Updating the records
def UpdateRecords(request, id):
	if request.method == 'POST':
		update = Student.objects.get(pk = id)
		form = StudentForm(request.POST, instance = update)
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			records = Student(name = name, email = email, password = password)
			records.save()
	else:
		update = Student.objects.get(pk = id)
		form = StudentForm(instance = update)
	return render(request, 'crud/Update.html', {'form':form})


#This is for deleting records
def DeleteRecords(request, id):
	if request.method == 'POST':
		delRecords = Student.objects.get(pk = id)
		delRecords.delete()
		return HttpResponseRedirect('/')


