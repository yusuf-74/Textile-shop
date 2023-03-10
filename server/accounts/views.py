from django.shortcuts import render,redirect
from django.views import View
from .models import Account ,Transaction
from .filters import AccountFilter
from django.contrib.auth.mixins import LoginRequiredMixin
class Test(LoginRequiredMixin,View):
    def get(self,request,*args, **kwargs):
        return render(request,'users/register-login.html')
        
    
    def post(self,request,*args, **kwargs):
        
        print(dict(request.POST))
        
        return render(request,'users/register-login.html')
    
    
# ACCOUNT_TYPE = {'Bank': 'Bank', 'e_wallet': 'E-Wallet','postal': 'Postal','bank':'Bank'}

class AccountsView(LoginRequiredMixin,View):
    def get(self,request,*args, **kwargs):
        
        accounts = AccountFilter(request.GET,queryset=Account.objects.all())
        
        
        accounts_data = [{'id': account.id \
            ,'type':account.type \
            ,'service_provider':account.service_provider \
            , 'account_number': account.account_number \
            , 'balance': account.balance \
            , 'created_by':account.created_by }\
                for account in accounts.qs]
        return render(request,'accounts/all-accounts.html',{'accounts':accounts_data})


class EditAccountView(LoginRequiredMixin,View):
    login_url= "login"
    
    def get(self,request,*args, **kwargs):
        return render(request,'accounts/create-account.html')
    
    def post(self,request,*args, **kwargs):
        data = dict(request.POST)
        
        
        
        if data['_method'][0] == 'POST':
            try : 
                account = Account.objects.create(
                    type = data['type'][0],
                    account_number = data['account_number'][0],
                    service_provider = data['service_provider'][0],
                    created_by = request.user)
                account.save()
                return redirect('all_accounts')
            except:
                return redirect('all_accounts')
            
        elif data['_method'][0] == 'PUT':
            try:
                account = Account.objects.get(id=data['id'][0])
                account.type = data['type'][0]
                account.account_number = data['account_number'][0]
                account.service_provider = data['service_provider'][0]
                account.save()
                if data['from'][0] == 'all':
                    return redirect('all_accounts')
                return redirect('detailed_accounts',pk=data['id'][0])
            except:
                if data['from'][0] == 'all':
                    return redirect('all_accounts')
                return redirect('detailed_accounts',pk=data['id'][0])
        
        
        elif data['_method'][0] == 'DELETE':
            try:
                account = Account.objects.get(id=data['id'][0])
                account.delete()
                return redirect('all_accounts')
            except:
                return redirect('all_accounts')
            
            
class AccountDetailView(LoginRequiredMixin,View):
    def get(self,request,*args, **kwargs):
        account = Account.objects.get(id=kwargs['pk'])
        transactions = account.transactions.all()
        print(transactions)
        return render(request,'accounts/detailed-account.html',{'account':account , 'transactions':transactions})
    
class CreateTransactionView(LoginRequiredMixin,View):
    def post(self,request,*args, **kwargs):
            data = dict(request.POST)
        # try:
            account = Account.objects.get(id=data['id'][0])
            transaction = Transaction.objects.create(
                account = account,
                amount = data['amount'][0],
                transaction_type = data['transaction_type'][0],
                description = data['description'][0],
                created_by = request.user)
            transaction.save()
            return redirect('detailed_accounts',pk=data['id'][0])
        # except:
            return redirect('detailed_accounts',pk=data['id'][0])