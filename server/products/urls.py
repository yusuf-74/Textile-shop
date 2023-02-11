from django.urls import path
from products.views import PillowView,PillowDetailView,\
    PillowUpdate,AllProdView,PillowDelete



urlpatterns=[
    path('products/' , AllProdView.as_view() , name='all_products'),
    path('types/<str:type>' , PillowView.as_view() , name='pillow'),
    path("all_pillows" , PillowView.as_view() , name='all_pillows'),
    path('pillow/<int:pk>/' , PillowDetailView.as_view() , name='pillow-detail'),
    path("pillow/<int:pk>/delete",PillowDelete.as_view() , name="pillow-delete"),
    path("pillow/<int:pk>/update" , PillowUpdate.as_view() , name="pillow-update")

]