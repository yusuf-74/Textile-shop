from django.db import models


class CustomerProfile(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    government = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


