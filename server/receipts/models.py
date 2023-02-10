from django.db import models

class CustomerReceipt(models.Model):
    customer = models.ForeignKey('employees.person', related_name='customer_receipt', on_delete=models.CASCADE)
    date = models.DateField()
    paid = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    pillow = models.OneToOneField('products.Pillow', related_name='customer_receipt', blank=True,null=True, on_delete=models.CASCADE)
    fiber_bag = models.OneToOneField('products.FiberBag', related_name='customer_receipt', blank=True,null=True, on_delete=models.CASCADE)
    
    class META:
        ordering = ['-date']

    
    def __str__(self):
        return self.customer.name

    
    @property
    def total(self):
        if not self.pillow and self.fiber_bag:
            return self.fiber_bag.retail_price * self.fiber_bag.quantity
        elif not self.fiber_bag and self.pillow:
            return self.pillow.retail_price * self.pillow.quantity
        elif self.fiber_bag and self.pillow:
            return self.fiber_bag.retail_price * self.fiber_bag.quantity + self.pillow.retail_price * self.pillow.quantity
        else :
            return 0
        

    @property
    def remaining(self):
        return self.paid - self.total

class SuppliersReceipt(models.Model):
    supplier = models.ForeignKey('employees.person',related_name='supplier_receipt' ,on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    paid = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    bag = models.OneToOneField('materials.Bag', related_name='supplier_receipt', blank=True,null=True, on_delete=models.CASCADE)
    fiber = models.OneToOneField('materials.Fiber', related_name='supplier_receipt', blank=True,null=True, on_delete=models.CASCADE)
    fibric = models.OneToOneField('materials.Fabric', related_name='supplier_receipt', blank=True,null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.supplier.name

    @property
    def total(self):
        purchases = [(self.bag or 0), (self.fiber or 0), (self.fibric or 0)]
        total = sum([0 if not purchase else purchase.price*purchase.quantity for purchase in purchases])
        
        return total

    @property
    def remaining(self):
        return self.paid - self.total

