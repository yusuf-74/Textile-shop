from django.contrib import admin
from .models import Perishable , Fabric, Fiber, Bag

class PerishableAdmin(admin.ModelAdmin):
    list_display = ('type', 'price', 'created_on', 'created_by', 'total')

admin.site.register(Perishable, PerishableAdmin)
admin.site.register(Fabric)
admin.site.register(Fiber)
admin.site.register(Bag)