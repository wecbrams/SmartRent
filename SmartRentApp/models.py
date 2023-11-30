from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.firstname + " " + self.surname


class Accommodation(models.Model):
    region = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.region} - ${self.price}"


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE)
    commission = models.DecimalField(max_digits=10, decimal_places=2)
    expiration_time = models.DateTimeField()
