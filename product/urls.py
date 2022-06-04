from django.urls import path

from product.views import ProductListView, ProductActionView, ProductDetailView, ProductCategoryListView

urlpatterns = [
    path('product/category/list/', ProductCategoryListView.as_view(), name='product_category_list'),
    path('product/list/<int:pk>/', ProductListView.as_view(), name='product_list'),
    path('product/detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/action/', ProductActionView.as_view(), name='product_action'),
]
