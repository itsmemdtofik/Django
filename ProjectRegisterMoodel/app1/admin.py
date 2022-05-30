from django.contrib import admin
from app1.models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'stuID', 'stuName','stuAddr', 'stuPass', 'stuComment', 'stuMobno')
    
#admin.site.register(Student, StudentAdmin)
