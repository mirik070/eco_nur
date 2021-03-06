from django.urls import path

from income.views import IncomeListView, IncomeActionView, IncomeDetailView, OutcomeListView

urlpatterns = [
    path('income/list/', IncomeListView.as_view(), name='income_list'),
    path('outcome/list/', OutcomeListView.as_view(), name='outcome_list'),
    path('income/detail/<int:pk>/', IncomeDetailView.as_view(), name='income_detail'),
    path('income/action/', IncomeActionView.as_view(), name='income_action'),
]
