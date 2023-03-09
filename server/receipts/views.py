from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import CustomerReceipt
from django.contrib.auth.mixins import LoginRequiredMixin

class OrdersView(LoginRequiredMixin,View):
    
    def get(self ,request,*args, **kwargs):
        data = [{'orderId':receipt.id  \
                , 'customerName': receipt.customer.name \
                , 'price': receipt.total \
                , 'status':'delivered'} \
                for receipt in CustomerReceipt.objects.all()]
        
        return render(request, 'receipts/customer-receipts.html', {'orders': data})
    

