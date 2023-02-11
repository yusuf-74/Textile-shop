from django.db import models
from .utils import products_image_file_path
from django.urls import reverse


types_of_pillows = [('pillow', 'pillow'), ('circular pillow', 'circular pillow')]
categories_of_pillows = [('fabric', 'fabric'), ('bag', 'bag') , ('fiber','fiber')]


class FiberBag(models.Model):
    retail_price = models.DecimalField(max_digits=6, decimal_places=2)
    wholesale_price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()
    type = models.CharField(max_length=100 , default="FiberBag") # cotton, jute, etc.
    description = models.TextField(null=True, blank=True)
    fiber = models.OneToOneField('materials.Fiber', on_delete=models.CASCADE)
    bag = models.OneToOneField('materials.Bag', on_delete=models.CASCADE)
    fibric = models.OneToOneField('materials.Fabric', on_delete=models.CASCADE)
    image_url=models.ImageField(upload_to=products_image_file_path , blank=True , null=True)

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
    fiber = models.OneToOneField('materials.Fiber', on_delete=models.CASCADE ,blank=True , null=True)
    bag = models.OneToOneField('materials.Bag', on_delete=models.CASCADE,blank=True , null=True)
    fibric = models.OneToOneField('materials.Fabric', on_delete=models.CASCADE , blank=True , null=True)
    image_url=models.ImageField(upload_to=products_image_file_path ,blank=True , null=True)




    def __str__(self):
        return self.size + ' ' + self.type + ' ' + self.category

    def get_url(self):
        return reverse('product-detail' , args=[self.id])
