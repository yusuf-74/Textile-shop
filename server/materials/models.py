from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Sum
import threading

choices = [('petrol', 'بنزين'), ('oil', 'زيت'), ('water', 'فاتورة مياه'),\
                ('electricity', 'فاتورة كهرباء'), ('food', 'أكل'), \
                ('delivery', 'توصيل'), ('rent', 'إيجار'), ('nails', 'مسامير'),\
                ('string', 'إبر'), ('transport', 'نقل'), ('other', 'اخر'),        
]

def get_current_user():
    return getattr(threading.local(), 'user', None)

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
    type = models.CharField(max_length=20, choices=choices)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    updated_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='updated_by')
    
    def __str__(self):
        return self.type + ': ' + str(self.created_on)
    

    @property
    def total(self):
        return Perishable.objects.aggregate(Sum('price'))['price__sum'] or 0
    
    def save(self, *args, **kwargs):
        if not self.created_by:
            self.created_by = get_current_user()
        if not self.updated_by:
            self.updated_by = get_current_user()
        super(Perishable, self).save(*args, **kwargs)