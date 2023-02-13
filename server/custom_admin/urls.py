from django.urls import path
from .views import DashboardView , LoginView , RegisterView , LogoutView

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='analytics'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
