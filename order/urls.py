from django.urls import path

from order.views import OrderCreatedListView, OrderActionView, OrderDetailView, OrderPendingListView, OrderListView

urlpatterns = [
    path('order/list/', OrderListView.as_view(), name='order_list'),
    path('order/created/list/', OrderCreatedListView.as_view(), name='order_created_list'),
    path('order/pending/list/', OrderPendingListView.as_view(), name='order_pending_list'),
    path('order/detail/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('order/action/', OrderActionView.as_view(), name='order_action'),
]
