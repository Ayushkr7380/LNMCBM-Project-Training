from django.db import models

# Create your models here.

class Member(models.Model):
    firstname = models.CharField(max_length = 225)
    lastname = models.CharField(max_length = 225)
    phone  = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Student(models.Model):
    name = models.CharField(max_length = 30)
    rollnumber = models.IntegerField()

0