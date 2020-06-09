from django.db import models
from django.core import validators
from django.core.exceptions import ValidationError 


def check(email):
    if 'A' not in email:
        raise ValidationError('Should incude A')
    else:
        pass


class Sign(models.Model):
    password=models.CharField(max_length=20)
    name=models.CharField(max_length=40)
    email=models.EmailField(max_length=50)
    

    def __str__(self):
        return self.password

class Session(models.Model):
    session= models.CharField(max_length=50,unique=True)

    def __str__(self):
         return self.session
    
class Student(models.Model):
    name=models.CharField(max_length=50,unique=False)
    session= models.ForeignKey("Session",on_delete=models.PROTECT)

    def __str__(self):
        return self.name



class Register(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50,validators=[check])
    verify_email=models.EmailField(max_length=50)




