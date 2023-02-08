from django.urls import path
from .views import MaterialsView
urlpatterns = [
    path('', MaterialsView.as_view(), name='materials'),
]
