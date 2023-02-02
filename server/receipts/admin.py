from django.contrib import admin
from .models import CustomerReceipt

class CustomerReceiptAdmin(admin.ModelAdmin):
    fields = ['customer', 'date', 'paid', 'description']
    list_display = ['customer', 'date', 'paid', 'total', 'remaining']
    

admin.site.register(CustomerReceipt, CustomerReceiptAdmin)
# Register your models here.
