from django.urls import path

from warehouse.views import RawListView, WarehouseActionView, WarehouseRawListView, WarehouseProductListView

urlpatterns = [
    path('raws/list/', RawListView.as_view(), name='raw_list'),
    path('warehouse/raw/list/', WarehouseRawListView.as_view(), name='warehouse_raw_list'),
    path('warehouse/product/list/', WarehouseProductListView.as_view(), name='warehouse_product_list'),
    path('warehouse/action/', WarehouseActionView.as_view(), name='warehouse_action')
]
