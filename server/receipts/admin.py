from django.contrib import admin
from .models import CustomerReceipt , SuppliersReceipt

class CustomerReceiptAdmin(admin.ModelAdmin):
    fields = ['customer', 'pillow' ,'fiber_bag' ,'date', 'paid']
    list_display = ['customer', 'date', 'paid', 'total', 'remaining']
    
class SuppliersReceiptAdmin(admin.ModelAdmin):
    fields = ['supplier', 'material', 'date', 'paid', 'total', 'remaining']
    list_display = ['supplier', 'date', 'paid', 'total', 'remaining']

admin.site.register(CustomerReceipt, CustomerReceiptAdmin)
admin.site.register(SuppliersReceipt, SuppliersReceiptAdmin)
# Register your models here.
