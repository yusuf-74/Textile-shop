from django.db import models

types_of_transactions = [('buy', 'buy'), ('return', 'return')]
class Material(models.Model):
    type = models.CharField(max_length=100)
    types_of_transactions = models.CharField(max_length=10, choices=types_of_transactions)
    supplier = models.ForeignKey('suppliers.SupplierProfile', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateField(auto_now=True)
    
    def __str__(self) -> str:
        return self.type
    
    