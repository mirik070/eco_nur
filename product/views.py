from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from product.helpers import create_product, update_product, create_product_weight, delete_product_weight, \
    create_product_category, update_product_category
from product.models import Product, ProductWeight, ProductCategory


class ProductCategoryListView(TemplateView):
    template_name = 'product_category_list.html'

    def get_context_data(self, **kwargs):
        context = super(ProductCategoryListView, self).get_context_data(**kwargs)
        context['product_categories'] = ProductCategory.objects.order_by('-id')
        return context


class ProductListView(TemplateView):
    template_name = 'product_list.html'

    def get_context_data(self, pk, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['products'] = Product.objects.filter(category_id=pk).order_by('-id')
        context['category'] = ProductCategory.objects.get(id=pk)
        return context


class ProductDetailView(TemplateView):
    template_name = 'product_detail.html'

    def get_context_data(self, pk, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['product'] = Product.objects.get(id=pk)
        context['product_weights'] = ProductWeight.objects.filter(product_id=pk)
        return context


class ProductActionView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ProductActionView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        post_request = self.request.POST
        user = self.request.user
        action = self.request.POST.get('action', None)
        print(action)
        actions = {
            'create_product_category': create_product_category,
            'update_product_category': update_product_category,
            'create_product': create_product,
            'update_product': update_product,
            'create_product_weight': create_product_weight,
            'delete_product_weight': delete_product_weight,
        }
        response = actions[action](post_request, user)
        back_url = response['back_url']
        return redirect(back_url)
