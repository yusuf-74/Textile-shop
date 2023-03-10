from django.urls import path
from . import views
urlpatterns = [
    path('test/', views.Test.as_view(), name='test'),
    path('', views.AccountsView.as_view(), name='all_accounts'),
    path('<int:pk>/', views.AccountDetailView.as_view(), name='detailed_accounts'),
    path('edit/', views.EditAccountView.as_view(), name='edit_account'),
    # path('transactions/', views.TransactionsView.as_view(), name='all_transactions'),
    path('transactions/create', views.CreateTransactionView.as_view(), name='create_transaction'),
]
