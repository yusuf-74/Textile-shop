from django.db import models
from .utils import products_image_file_path
from django.urls import reverse
import products


types_of_pillows = [('pillow', 'pillow'), ('circular pillow', 'circular pillow')]


class FiberBag(models.Model):
    retail_price = models.DecimalField(max_digits=6, decimal_places=2)
    wholesale_price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()
    type = models.CharField(max_length=100 , default="FiberBag",blank=True) # cotton, jute, etc.
    description = models.TextField(null=True, blank=True)
    fiber = models.OneToOneField('materials.Fiber', null=True , blank=True,on_delete=models.CASCADE)
    bag = models.OneToOneField('materials.Bag', null=True , blank=True,on_delete=models.CASCADE)
    fibric = models.OneToOneField('materials.Fabric', null=True , blank=True,on_delete=models.CASCADE)
    image_url=models.ImageField(blank=True, null=True, upload_to=products.utils.products_image_file_path)


    def __str__(self):
        return self.type


class Pillow(models.Model):
    retail_price = models.DecimalField(max_digits=6, decimal_places=2)
    wholesale_price = models.DecimalField(max_digits=6, decimal_places=2)
    type = models.CharField(choices= types_of_pillows , max_length=20)
    quantity = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    size = models.CharField(max_length=100) # example  50 x 60
    image_url=models.ImageField(blank=True, null=True, upload_to=products.utils.products_image_file_path)
    fiber = models.OneToOneField('materials.Fiber', null=True , blank=True,on_delete=models.CASCADE)
    bag = models.OneToOneField('materials.Bag', null=True , blank=True,on_delete=models.CASCADE)
    fibric = models.OneToOneField('materials.Fabric', null=True , blank=True,on_delete=models.CASCADE)



    def __str__(self):
        return self.size + ' ' + self.type + ' '
    def get_url(self):
        return reverse('product-detail' , args=[self.id])

