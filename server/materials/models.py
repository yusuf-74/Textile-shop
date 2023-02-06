from django.db import models
from django.contrib.auth import get_user_model

# perishables = [('petrol', 'petrol'), ('oil', 'oil'), ('water', 'water'),\
#                 ('electricity', 'electricity'), ('food', 'food'), \

#         ]

class Fabric(models.Model):
    supplier = models.ForeignKey('employees.person', on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

class Fiber(models.Model):
    supplier = models.ForeignKey('employees.person', on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

class Bag(models.Model):
    supplier = models.ForeignKey('employees.person', on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

class Perishable(models.Model):
    petrol = models.IntegerField()
    delivery = models.IntegerField()
    electricity = models.IntegerField()
    water = models.IntegerField()
    rent = models.IntegerField()
    nails = models.IntegerField()
    string = models.IntegerField()
    transport = models.IntegerField()
    other = models.IntegerField()
    date = models.DateField(auto_now=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    def __str__(self):
        return 'perishable : ' + str(self.date)

    @property
    def total (self):
        return self.petrol + self.delivery + self.electricity + self.water + self.rent + self.nails + self.string + self.transport + self.other



