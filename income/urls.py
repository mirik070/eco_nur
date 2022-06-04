from django.urls import path

from income.views import IncomeListView, IncomeActionView, IncomeDetailView

urlpatterns = [
    path('income/list/', IncomeListView.as_view(), name='income_list'),
    path('income/detail/<int:pk>/', IncomeDetailView.as_view(), name='income_detail'),
    path('income/action/', IncomeActionView.as_view(), name='income_action'),
]
