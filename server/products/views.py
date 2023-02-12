from django.shortcuts import render,get_object_or_404, redirect
from django.views import View
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import FiberBag
from django.views.generic.edit import FormMixin
from django.db.models import Q
from products.models import Pillow
from django.core import serializers
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect



class ProductsView(View):

    def get(self,request,*args, **kwargs):
        return render(request, 'admin/products.html')


class FiberbagListView(ListView):
    model = FiberBag
    template_name = 'products/fiberbags/fiberbag_list.html'
    context_object_name = 'fiberbags'
    paginate_by = 2
    ordering = ['id']

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(type__icontains=search_query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(self.object_list, self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        return context

class EditFiberBagView(View):
    def get(self,request,*args, **kwargs):
        return render(request,'products/fiberbags/fiberbag_form.html')

    def post(self,request,*args, **kwargs):

        data = dict(request.POST)

        if data['_method'][0] == 'POST':
            try:
                fiberbag = FiberBag.objects.create(type = data['type'][0]\
                ,quantity = data['quantity'][0]\
                ,retail_price = data['retail_price'][0]\
                ,wholesale_price = data['wholesale_price'][0]\
                    )
            except:
                raise Exception('error')

            return redirect('fiberbag_list')

        elif data['_method'][0] == 'PUT':
            fiberbag = FiberBag.objects.get(id = data['id'][0])
            fiberbag.type = data['type'][0]
            fiberbag.quantity = data['quantity'][0]
            fiberbag.retail_price = data['retail_price'][0]
            fiberbag.wholesale_price = data['wholesale_price'][0]
            fiberbag.save()

            return redirect('fiberbag_list')

        elif data['_method'][0] == 'DELETE':
            fiberbag = FiberBag.objects.get(id = data['id'][0])
            fiberbag.delete()
            return redirect('fiberbag_list')

        return redirect('fiberbag_list')

class FiberBagDetailView(DetailView):
    model = FiberBag
    template_name = 'products/fiberbags/fiberbag_detail.html'

class PillowView(ListView):
    template_name='products/pillow/pillow.html'
    context_object_name='prods'
    model=Pillow
    paginate_by=2


    def get_queryset(self):
        queryset = super().get_queryset()
        type=self.kwargs.get('type' , None)
        if type:
            return queryset.filter(type=type).order_by('-id')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product_nums"] = self.get_queryset().count()
        context["type"]=self.kwargs.get('type')
        return context

class PillowDetailView(DetailView):
    template_name='products/pillow/pillow_detail.html'
    context_object_name='product'
    model=Pillow

class PillowUpdate(UpdateView):
    template_name='products/pillow/pillow.html'
    model=Pillow
    fields=["retail_price" , "wholesale_price","size" , "quantity"]
    def get_success_url(self):
        type=self.get_object().type
        return reverse_lazy("pillow" , kwargs={"type":type})

class PillowDelete(DeleteView):
    template_name='products/pillow/pillow.html'
    model=Pillow

    def delete(self, request, *args, **kwargs):

        self.object = self.get_object()
        type=self.object.type
        success_url =reverse_lazy("pillow" , kwargs={"type":type})
        self.object.delete()
        return HttpResponseRedirect(success_url)
class PillowCreate(CreateView):
    fields=["retail_price" , "wholesale_price","size" , "quantity" , "description" , "category"]
    model=Pillow
    template_name='products/pillow/create_pillow.html'

    def form_valid(self, form):
        """If the form is valid, save the associated model."""

        self.object = form.save()
        if "circular pillow" in self.request.path:
                self.object.type="circular pillow"
        else:
            self.object.type="pillow"
        self.object.save()
        success_url=reverse_lazy("pillow" , kwargs={"type":self.object.type})
        return HttpResponseRedirect(success_url)




