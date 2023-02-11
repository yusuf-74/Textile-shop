from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,TemplateView,DetailView,\
    UpdateView,TemplateView,DeleteView
from django.views.generic.edit import FormMixin
from django.db.models import Q
from products.models import Pillow
from django.core import serializers
from django.urls import reverse_lazy

class AllProdView(TemplateView):
    template_name="admin/products.html"


class PillowView(ListView):
    template_name='products/pillow.html'
    context_object_name='prods'
    model=Pillow
    queryset=Pillow.objects.all()
    paginate_by=1


    def get_queryset(self):
        type=self.kwargs.get('type' , None)
        if type:
            return self.queryset.filter(type=type).order_by('-id')

        return self.queryset.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product_nums"] = self.get_queryset().count()
        return context

class PillowDetailView(DetailView):
    template_name='products/pillowdetail.html'
    context_object_name='product'
    model=Pillow


    def get_object(self , queryset=None):
        pk=self.kwargs.get('pk')
        print(pk)
        return self.model.objects.get(pk=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class PillowUpdate(UpdateView):
    template_name='products/pillow.html'
    model=Pillow
    success_url=reverse_lazy("pillow")
    fields=["retail_price" , "wholesale_price","size" , "quantity"]

class PillowDelete(DeleteView):
    template_name='products/pillow.html'
    model=Pillow
    success_url=reverse_lazy("all_pillows")


    # def form_valid(self, form):
    #     success_url = self.get_success_url()
    #     type=self.object.type
    #     self.object.delete()
    #     return HttpResponseRedirect(reverse(success_url, kwargs={'type':type}))


