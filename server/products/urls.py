from django.urls import path
from .views import\
    ProductsView,\
    FiberbagListView,\
    FiberBagDetailView,\
    EditFiberBagView


urlpatterns = [
    path('', ProductsView.as_view(), name='products'),
    path('fiberbags/', FiberbagListView.as_view(), name='fiberbag_list'),
    path('fiberbags/edit/',EditFiberBagView.as_view(), name='fiberbag_edit'),
    path('fiberbags/<int:pk>/', FiberBagDetailView.as_view(), name='fiberbag_detail'),
    ]

