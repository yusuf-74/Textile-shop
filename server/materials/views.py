from django.shortcuts import render,get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView
from .models import Perishable, choices
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

class MaterialsView(View):
    def get(self, request):
        return render(request, 'admin/materials.html')
    
class PerishableListView(ListView):
    model = Perishable
    template_name = 'materials/perishables/perishables_list.html'
    context_object_name = 'perishables'
    paginate_by = 5
    ordering = ['id']

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(self.object_list, self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        total = Perishable.objects.aggregate(Sum('price'))['price__sum'] or 0
        context['total'] = total
        return context
    
@login_required
def perishable_create(request):
    if request.method == 'POST':
        type = request.POST.get('type')
        price = request.POST.get('price')
        created_by = request.user
        updated_by = request.user
        Perishable.objects.create(type=type, price=price, created_by=created_by, updated_by=updated_by)
        return redirect('perishable_list')

    context = {'choices': choices}
    return render(request, 'materials/perishables/perishable_form.html', context)    

class EditPerishableView(View):
    def get(self,request,*args, **kwargs):
        return render(request,'materials/perishables/perishable_form.html', {'choices': choices})

    def post(self,request,*args, **kwargs):

        data = dict(request.POST)

        if data['_method'][0] == 'PUT':
            perishable = Perishable.objects.get(id = data['id'][0])
            perishable.type = data['type'][0]
            perishable.price = data['price'][0]
            perishable.updated_by = request.user
            perishable.save()

            return redirect('perishable_list')
        
        

        elif data['_method'][0] == 'DELETE':
            perishable = Perishable.objects.get(id = data['id'][0])
            perishable.delete()
            return redirect('perishable_list')

        return redirect('perishable_list')
