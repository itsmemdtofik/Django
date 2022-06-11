from django.db import models

class Student(models.Model):
	ID = models.IntegerField(primary_key=True)
	name = models.CharField(max_length = 100)
	address = models.CharField(max_length = 100)
	contact = models.IntegerField()
	email = models.EmailField(max_length = 100)
	passwd = models.CharField(max_length = 100)
	comment = models.CharField(max_length = 100)

	def __str__(self):
		return self.name



