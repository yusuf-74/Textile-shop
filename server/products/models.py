from django.db import models




types_of_pillows = [('مخدة', 'مخدة'), ('خددية', 'خددية')] # زرط خام  
categories_of_pillows = [('قماش', 'قماش'), ('كبس', 'كبس') , ('فايبر','فايبر')] # زرط خام  


class FiberBag(models.Model):
    retail_price = models.DecimalField(max_digits=6, decimal_places=2)
    wholesale_price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()
    type = models.CharField(max_length=100) # cotton, jute, etc.
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.type

class Pillow(models.Model):
    category = models.CharField(choices=categories_of_pillows , max_length=100)
    retail_price = models.DecimalField(max_digits=6, decimal_places=2)
    wholesale_price = models.DecimalField(max_digits=6, decimal_places=2)
    type = models.CharField(choices= types_of_pillows , max_length=20) 
    quantity = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    size = models.CharField(max_length=100) # example  50 x 60

    def __str__(self):
        return self.size + ' ' + self.type + ' ' + self.category
    
