from django.shortcuts import render
from django.views import View
from receipts.models import CustomerReceipt, SuppliersReceipt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout 
class DashboardView(View):
    def get(self, request):
        orders_data = [{'orderId' : receipt.id , 'customer':receipt.customer.name , 'price':receipt.total , 'status':'delivered' } for receipt in CustomerReceipt.objects.all().order_by('-date')]
        if len(orders_data) > 5:
            orders_data = orders_data[:5]
        sales = sum([ receipt.total for receipt in CustomerReceipt.objects.all()])
        purchases = sum([ receipt.total for receipt in SuppliersReceipt.objects.all()])
        net_profit = sales - purchases
        
        user = {'name': 'Admin', 'email': ''}
        
        return render(request, 'admin/analytics.html', {'data':{'orders_data': orders_data, 'sales': sales, 'purchases': purchases, 'net_profit': net_profit}})

class LoginView(View):
    def get(self, request):
        return render(request, 'users/register-login.html')
    
    def post(self, request):
        data = dict(request.POST)
        
        username = data['username'][0]
        password = data['password'][0]
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'admin/analytics.html')
        else:
            return render(request, 'users/register-login.html', {'error': 'Invalid username or password'})

class RegisterView(View):
    def get(self, request):
        return render(request, 'users/register-login.html')
    
    def post(self, request):
        data = dict(request.POST)
        
        username = data['username'][0]
        password = data['password'][0]
        repeat_password = data['repeat_password'][0]
        email = data['email'][0]
        
        user = User.objects.create_user(username, email, password)
        user.save()
        
        login(request, user)
        
        return render(request, 'admin/analytics.html', {'success': 'User created successfully'})
    
class LogoutView(View):
    def get(self, request):
        logout(request)
        return render(request, 'users/register-login.html')