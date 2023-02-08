from django.shortcuts import render
from django.views import View

class ProductsView(View):
    
    def get(self,request,*args, **kwargs):
        return render(request, 'admin/products.html')
