from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,TemplateView,DetailView
from django.views.generic.edit import FormMixin
from django.db.models import Q
from products.models import Pillow



class PillowView(ListView):
    template_name='products/pillow.html'
    context_object_name='prod'
    model=Pillow
    queryset=Pillow.objects.all()
    paginate_by=1


    def get_queryset(self):
        type=self.kwargs.get('type' , None)
        if type:
            return self.queryset.filter(type=type).order_by('-id')
        # search=self.request.GET.get('search' , None)
        # # if search:
        #     return self.queryset.filter(\
        #          Q(product_name__icontains=search) | Q(description__icontains=search)).order_by('-id')
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

