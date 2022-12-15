from django.db import models

# Create your models here.
class Course(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=300)
    duration=models.IntegerField()
    fee=models.IntegerField()
    image=models.ImageField()

class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    phno=models.CharField(max_length=10)

class Staff(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    phno=models.CharField(max_length=10)
    password=models.CharField(max_length=20)
  