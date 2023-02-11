from django.contrib import admin
from .models import Perishable , Fabric, Fiber, Bag

admin.site.register(Perishable)
admin.site.register(Fabric)
admin.site.register(Fiber)
admin.site.register(Bag)
