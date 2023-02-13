from django.shortcuts import render
from django.views import View

class Test(View):
    def get(self,request,*args, **kwargs):
        return render(request,'users/register-login.html')
        
    
    def post(self,request,*args, **kwargs):
        
        print(dict(request.POST))
        
        return render(request,'users/register-login.html')
