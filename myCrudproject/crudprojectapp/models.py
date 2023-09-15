from django.db import models

# Create your models here.
class Student(models.Model):  
    fname = models.CharField(max_length=100)  
    lname = models.CharField(max_length=100)
    gender = models.CharField(max_length=5)  
    address = models.CharField(max_length=100)
    email = models.EmailField()  
    contact = models.PositiveIntegerField() 
   
    class Meta:  
        db_table = "tblstudent"