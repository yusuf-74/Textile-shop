from django.urls import path
from products.views import PillowView,PillowDetailView


urlpatterns=[
    path('' , PillowView.as_view() , name='store'),
    path('types/<str:type>' , PillowView.as_view() , name='products-by-types'),
    path('pillow/<int:pk>/' , PillowDetailView.as_view() , name='product-detail'),
    # path('search/' , HomeView.as_view() , name='search'),
    # path("graphql", GraphQLView.as_view(graphiql=True , schema=schema)),

]