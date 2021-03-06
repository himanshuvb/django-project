from django.db import models
from random import choices

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    roll = models.IntegerField(default=0)
    regno = models.IntegerField(default=0)
    age = models.IntegerField(default=1,blank=True,null=True)
    div = models.IntegerField(default =0,choices=[(1,1),(2,2),(3,3),(4,4),(5,5)])
    profile = models.ImageField(default=None, null=True)


    def __str__(self):
        return str(self.regno)

class Leaves(models.Model):
    regno = models.ForeignKey(Student,on_delete=models.CASCADE)
    roll = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    div = models.IntegerField(default =0,choices=[(1,1),(2,2),(3,3),(4,4),(5,5)])

    def __str__(self):
        return self.name


class Git(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    message = models.CharField(max_length=2000)

    def __str__(self):
        return self.name