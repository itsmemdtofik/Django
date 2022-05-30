from django.db import models

class Student(models.Model):
    stuID = models.IntegerField()
    stuName = models.CharField(max_length=100)
    stuAddr = models.CharField(max_length=100)
    stuPass = models.CharField(max_length=100)
    stuComment = models.CharField(max_length=100)
    stuMobno = models.IntegerField()
    
    def __str__(self):
        return self.stuName
    

