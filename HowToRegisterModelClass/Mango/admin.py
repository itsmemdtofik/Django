from django.contrib import admin
from Mango.models import Student

#class StudentAdmin(admin.ModelAdmin):
#	list_display = ('ID', 'name', 'address', 'contact', 'email', 'passwd', 'comment')
#admin.site.register(Student, StudentAdmin)

@admin.register(Student)

class StudentAdmin(admin.ModelAdmin):
	list_display = ('ID', 'name', 'address', 'contact', 'email', 'passwd', 'comment')
