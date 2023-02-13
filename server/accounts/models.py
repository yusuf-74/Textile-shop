from django.db import models
from django.contrib.auth.models import User

ACCOUNT_TYPE = [('bank', 'Bank'), ('e_wallet', 'E-Wallet'),('postal', 'Postal')]

class Account(models.Model):
    type = models.CharField(max_length=50,choices=ACCOUNT_TYPE)
    balance = models.DecimalField(max_digits=11, decimal_places=2)
    account_number = models.CharField(max_length=50)
    service_provider = models.CharField(max_length=50)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.service_provider + ' ' + self.account_number
