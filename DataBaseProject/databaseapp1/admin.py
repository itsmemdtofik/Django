from django.contrib import admin
from .models import StudentForm

#admin.site.register(StudentForm)
@admin.register(StudentForm)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','studentID', 'studentName', 'studentPass', 'studentAddr', 'studentMobono')
# Register your models here.
