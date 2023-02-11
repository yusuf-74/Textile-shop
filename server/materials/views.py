from django.shortcuts import render
from django.views import View

class MaterialsView(View):
    def get(self, request):
        return render(request, 'admin/materials.html')

