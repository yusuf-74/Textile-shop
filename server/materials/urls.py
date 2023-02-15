from django.urls import path
from .views import MaterialsView, PerishableListView, EditPerishableView, perishable_create
urlpatterns = [
    path('', MaterialsView.as_view(), name='materials'),
    path('perishables/', PerishableListView.as_view(), name='perishable_list'),
    path('perishables/edit/',EditPerishableView.as_view(), name='perishable_edit'),
    path('perishables/create/', perishable_create, name='perishable_create')

]
