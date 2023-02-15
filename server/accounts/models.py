from django.db import models
from django.contrib.auth.models import User

ACCOUNT_TYPE = [('bank', 'Bank'), ('e_wallet', 'E-Wallet'),('postal', 'Postal')]
TRANSACTION_TYPE = [('deposit', 'Deposit'), ('withdraw', 'Withdraw')]
class Account(models.Model):
    type = models.CharField(max_length=50,choices=ACCOUNT_TYPE)
    account_number = models.CharField(max_length=50)
    service_provider = models.CharField(max_length=50)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.service_provider + ' ' + self.account_number
    
    @property
    def balance(self):
        total = 0
        for transaction in self.transactions.all():
            if transaction.transaction_type == 'deposit':
                total += transaction.amount
            else:
                total -= transaction.amount
        return total
    
class Transaction(models.Model):
    account = models.ForeignKey(Account,related_name ='transactions' , on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=50,choices=TRANSACTION_TYPE)
    amount = models.DecimalField(max_digits=11, decimal_places=2)
    description = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.description
