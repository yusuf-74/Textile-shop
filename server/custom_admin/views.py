from django.shortcuts import render
from django.views import View
from receipts.models import CustomerReceipt, SuppliersReceipt
class DashboardView(View):
    def get(self, request):
        orders_data = [{'orderId' : receipt.id , 'customer':receipt.customer.name , 'price':receipt.total , 'status':'delivered' } for receipt in CustomerReceipt.objects.all().order_by('-date')]
        if len(orders_data) > 5:
            orders_data = orders_data[:5]
        sales = sum([ receipt.total for receipt in CustomerReceipt.objects.all()])
        purchases = sum([ receipt.total for receipt in SuppliersReceipt.objects.all()])
        net_profit = sales - purchases
        return render(request, 'admin/analytics.html', {'data':{'orders_data': orders_data, 'sales': sales, 'purchases': purchases, 'net_profit': net_profit}})
    