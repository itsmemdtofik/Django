from django.db import models


class Student(models.Model):
    stuid = models.IntegerField()
    stuname = models.CharField(max_length=100)
    stuaddr = models.CharField(max_length=100)
    stupass = models.CharField(max_length=100)
    stucomment = models.CharField(max_length=100)
    stumobno = models.IntegerField()
