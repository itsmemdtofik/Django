from django.contrib import admin
from .models import StudentRegistration


@admin.register(StudentRegistration)



class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email','password')
