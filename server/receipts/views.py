from django.shortcuts import render
from django.http import HttpResponse
from .models import CustomerReceipt
def test(request):
    receipts = CustomerReceipt.objects.all()
    paid = sum([r.paid for r in receipts])
    total = sum([r.total for r in receipts])
    remaining = sum([r.remaining for r in receipts])
    
    return HttpResponse(f"Paid: {paid}, Total: {total}, Remaining: {remaining}")


