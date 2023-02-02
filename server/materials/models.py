from django.db import models

class Material(models.Model):
    type = models.CharField(max_length=100)
    supplier = models.ForeignKey('suppliers.SupplierProfile', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self) -> str:
        return self.type
    
