from django.db import models


# Create your models here.
class Student(models.Model):
    regno = models.CharField(max_length=8, default="21BCA201")
    name = models.CharField(
        max_length=100,
    )
    dob = models.DateField()
    department = models.CharField(
        max_length=50, default="BCA"
    )
    address = models.CharField(
        max_length=100,
    )
    phone = models.CharField(
        max_length=10,
    )

    def __str__(self):
        return self.name
