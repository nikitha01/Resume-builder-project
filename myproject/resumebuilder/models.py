from django.db import models

class Usertable(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Resumetable(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    phone=models.IntegerField()
    email=models.EmailField(max_length=100)

    degree=models.CharField(max_length=100)
    institute_1=models.CharField(max_length=100)
    marks_1=models.DecimalField(max_digits = 5, decimal_places = 2)

    puc=models.CharField(max_length=100)
    institute_2=models.CharField(max_length=100)
    marks_2=models.DecimalField(max_digits = 5, decimal_places = 2)

    school=models.CharField(max_length=100)
    institute_3=models.CharField(max_length=100)
    marks_3=models.DecimalField( max_digits = 5, decimal_places = 2)

    experience=models.CharField(max_length=200)
    skills=models.CharField(max_length=200)
    project=models.CharField(max_length=300)
    objective=models.CharField(max_length=1000)
    hobbies=models.CharField(max_length=100)

    def __str__(self):
        return self.name