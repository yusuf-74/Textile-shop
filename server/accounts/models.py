from django.db import models

account_type = [('bank', 'Bank'), ('e_wallet', 'E-Wallet'),('postal', 'Postal')]

class Account(models.Model):
    type = models.CharField(max_length=50,choices=account_type)
    balance = models.DecimalField(max_digits=11, decimal_places=2)
    account_number = models.CharField(max_length=50)
    service_provider = models.CharField(max_length=50)
    created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.service_provider + ' ' + self.account_number
