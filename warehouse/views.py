from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from warehouse.helpers import create_raw, update_raw
from warehouse.models import Raw, WarehouseRaw, WarehouseProduct


class RawListView(TemplateView):
    template_name = 'raw_list.html'

    def get_context_data(self, **kwargs):
        context = super(RawListView, self).get_context_data(**kwargs)
        context['raws'] = Raw.objects.all()
        return context


class WarehouseRawListView(TemplateView):
    template_name = 'warehouse_raw_list.html'

    def get_context_data(self, **kwargs):
        context = super(WarehouseRawListView, self).get_context_data(**kwargs)
        context['warehouse_raws'] = WarehouseRaw.objects.select_related('raw').all()
        return context


class WarehouseProductListView(TemplateView):
    template_name = 'warehouse_product_list.html'

    def get_context_data(self, **kwargs):
        context = super(WarehouseProductListView, self).get_context_data(**kwargs)
        context['warehouse_products'] = WarehouseProduct.objects.select_related('product',
                                                                                'product_color',
                                                                                'product_weight').all()
        return context


class WarehouseActionView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(WarehouseActionView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        post_request = self.request.POST
        user = self.request.user
        action = self.request.POST.get('action', None)
        print(action)
        actions = {
            'create_raw': create_raw,
            'update_raw': update_raw,
        }
        response = actions[action](post_request, user)
        back_url = response['back_url']
        return redirect(back_url)
