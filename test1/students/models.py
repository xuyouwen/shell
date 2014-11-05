from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    birth = models.DateTimeField()
    sex = models.CharField(max_length=1)
    email = models.EmailField()
    website = models.URLField()

    def __str__(self):
        return self.full_name
    class Admin:
        pass
