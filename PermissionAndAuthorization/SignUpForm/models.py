from statistics import mode
from django.db import models
from matplotlib.pyplot import title


class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
