from django.db import models
import datetime
class Patient(models.Model):
    date = models.DateField(default=datetime.date.today())
    regno = models.IntegerField(default=None)
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    doctor = models.CharField(max_length=50,default=None)
    address = models.TextField()
