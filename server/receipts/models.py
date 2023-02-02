from django.db import models

class CustomerReceipt(models.Model):
    customer = models.ForeignKey('customers.CustomerProfile', related_name='customer_receipt', on_delete=models.CASCADE)
    date = models.DateField()
    
    paid = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.customer.name
    
    @property
    def total(self):
        return sum([p.retail_price * p.quantity for p in self.pillow.all()]) + sum([f.retail_price * f.quantity for f in self.fiber_bag.all()])
    
    @property
    def remaining(self):
        return self.paid - self.total

class SuppliersReceipt(models.Model):
    supplier = models.ForeignKey('suppliers.SupplierProfile',related_name='supplier_receipt' ,on_delete=models.CASCADE)
    date = models.DateField()
    paid = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.supplier.name
    
    @property
    def total(self):
        return sum([p.price * p.quantity for p in self.material.all()])
    
    @property
    def remaining(self):
        return self.paid - self.total
