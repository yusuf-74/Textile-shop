from django.urls import path
from products.views import FiberbagListView, FiberBagDetailView, FiberBagCreateView, FiberBagUpdateView, FiberBagDeleteView

app_name = 'fiberbags'

urlpatterns = [
    path('fiberbags/', FiberbagListView.as_view(), name='fiberbag_list'),
    path('fiberbags/<int:pk>/', FiberBagDetailView.as_view(), name='fiberbag_detail'),
    path('fiberbags/create/', FiberBagCreateView.as_view(), name='fiberbag_create'),
    path('fiberbags/<int:pk>/update/', FiberBagUpdateView.as_view(), name='fiberbag_update'),
    path('fiberbags/<int:pk>/delete/', FiberBagDeleteView.as_view(), name='fiberbag_delete'),
]
