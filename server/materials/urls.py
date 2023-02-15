from django.urls import path
from .views import MaterialsView, PerishableListView, EditPerishableView
urlpatterns = [
    path('', MaterialsView.as_view(), name='materials'),
    path('perishables/', PerishableListView.as_view(), name='perishable_list'),
    path('perishables/edit/',EditPerishableView.as_view(), name='perishable_edit'),

]
