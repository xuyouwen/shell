from django.db import models

# Create your models here

class Students(models.Model):
    name=models.CharField(max_length=30)
    city=models.CharField(max_length=60)
    school=models.CharField(max_length=50)
    age=models.IntegerField(max_length=2)
    height=models.IntegerField(max_length=3)
    phone=models.CharField(max_length=11)
    email=models.EmailField()
    qq=models.CharField(max_length=15)
    workexp=models.CharField(max_length=50)
    careerexp=models.CharField(max_length=50)

class Organization(models.Model):
    name=models.CharField(max_length=30)
    code=models.CharField(max_length=30)
    industry=models.CharField(max_length=30)
    property=models.CharField(max_length=30)
    size=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    linkman=models.CharField(max_length=10)
    phone=models.CharField(max_length=11)
    intro=models.CharField(max_length=100)