from django.db import models
from django.forms import PasswordInput


class StudentRegistration(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.name