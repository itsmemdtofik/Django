from django.db import models

class StudentForm(models.Model):
    studentID = models.IntegerField()
    studentName = models.CharField(max_length=100)
    studentPass = models.CharField(max_length=100)
    studentAddr = models.CharField(max_length=100)
    studentMobono = models.IntegerField()
    def __str__(self):
        return self.studentName 
    


    
    
   
    
