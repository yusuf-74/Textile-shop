from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import FiberBag
from django.shortcuts import get_object_or_404, redirect
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


class FiberBagDetailView(DetailView):
    model = FiberBag
    template_name = 'products/fiberbags/fiberbag_detail.html'

class FiberBagCreateView(CreateView):
    model = FiberBag
    template_name = 'products/fiberbags/fiberbag_form.html'
    fields = ['retail_price', 'wholesale_price', 'quantity', 'type', 'description']
    success_url = reverse_lazy('fiberbags:fiberbag_list')


class FiberBagUpdateView(UpdateView):
    model = FiberBag
    template_name = 'products/fiberbags/fiberbag_update.html'
    fields = ['retail_price', 'wholesale_price', 'quantity', 'type', 'description']

    def get_success_url(self):
        return reverse_lazy('fiberbags:fiberbag_detail', kwargs={'pk': self.object.pk})

    def get_object(self, queryset=None):
        return get_object_or_404(FiberBag, pk=self.kwargs.get('pk'))

class FiberBagDeleteView(DeleteView):
    model = FiberBag
    template_name = 'products/fiberbags/fiberbag_confirm_delete.html'
    success_url = reverse_lazy('fiberbags:fiberbag_list')

    def get_object(self, queryset=None):
        return get_object_or_404(FiberBag, pk=self.kwargs.get('pk'))
