from django.urls import path
from .views import\
    ProductsView,\
    FiberbagListView,\
    FiberBagDetailView,\
    EditFiberBagView,\
    PillowDelete,PillowDetailView,\
    PillowUpdate,PillowView,\
    PillowCreate


urlpatterns = [
    path('', ProductsView.as_view(), name='products'),
    path('fiberbags/', FiberbagListView.as_view(), name='fiberbag_list'),
    path('fiberbags/edit/',EditFiberBagView.as_view(), name='fiberbag_edit'),
    path('fiberbags/<int:pk>/', FiberBagDetailView.as_view(), name='fiberbag_detail'),
    path('types/<str:type>' , PillowView.as_view() , name='pillow'),
    path("all_pillows" , PillowView.as_view() , name='all_pillows'),
    path('pillow/<int:pk>/' , PillowDetailView.as_view() , name='pillow-detail'),
    path("pillow/<int:pk>/delete",PillowDelete.as_view() , name="pillow-delete"),
    path("pillow/<int:pk>/update" , PillowUpdate.as_view() , name="pillow-update"),
    path("pillow/create" , PillowCreate.as_view() , name="pillow-create"),
    path("circular pillow/create" , PillowCreate.as_view() , name="circular-pillow-create"),
    ]

