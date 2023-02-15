from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Sum

perishables = [('petrol', 'petrol'), ('oil', 'oil'), ('water', 'water'),\
                ('electricity', 'electricity'), ('food', 'food'), \
                ('delivery', 'delivery'), ('rent', 'rent'), ('nails', 'nails'),\
                ('string', 'string'), ('transport', 'transport'), ('other', 'other'),        
]

class Fabric(models.Model):
    type = models.CharField(max_length=50)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

class Fiber(models.Model):
    type = models.CharField(max_length=50)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

class Bag(models.Model):
    type = models.CharField(max_length=50)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

class Perishable(models.Model):
    type = models.CharField(max_length=20, choices=perishables)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    
    def __str__(self):
        return self.type + ': ' + str(self.created_on)
    

    @property
    def total(self):
        return Perishable.objects.aggregate(Sum('price'))['price__sum'] or 0