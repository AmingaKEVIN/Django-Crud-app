from django.db import models

# Create your models here.
class Student(models.Model):
   
   name=models.CharField(max_length=100)
   email=models.EmailField(max_length=254)
   age=models.IntegerField()
   gender=models.CharField(max_length=10)
   
   def __str__(self):
      return self
   