from django.db import models


class Adress(models.Model):
    city = models.CharField(max_length=128)
    street = models.CharField(max_length=128)
    house_number = models.IntegerField()
    flat_number = models.IntegerField()
    
class Person(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=64)
    description = models.TextField()
    adress = models.ForeignKey(Adress)
    
class PhoneNumber(models.Model):
    number = models.IntegerField()
    type = models.CharField(max_length=64)
    person = models.ForeignKey(Person)
     
class Email(models.Model):
    email = models.EmailField()
    type = models.CharField(max_length=64)
    person = models.ForeignKey(Person)
    
    
    