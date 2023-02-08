from django.shortcuts import render
from django.views import View

class DashboardView(View):
    def get(self, request):
        return render(request, 'admin/analytics.html')

# class SearchView(View):
#     def get(self, request):
#         return render(request, 'admin/search.html')
