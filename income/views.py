from django.db.models import Subquery, OuterRef
from django.http import JsonResponse
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from income.helpers import create_income, get_product_weight_and_color_info, create_income_product_item, \
    delete_income_product_item, create_income_raw_item, delete_income_raw_item, change_income_status, \
    get_remainder_count_product
from income.models import Income, IncomeProductItem, IncomeRawItem
from product.models import Product
from warehouse.models import Raw, WarehouseRaw


class IncomeListView(TemplateView):
    template_name = 'income_list.html'

    def get_context_data(self, **kwargs):
        context = super(IncomeListView, self).get_context_data(**kwargs)
        context['incomes'] = Income.objects.filter(income_type='income').select_related('user')
        return context


class OutcomeListView(TemplateView):
    template_name = 'outcome_list.html'

    def get_context_data(self, **kwargs):
        context = super(OutcomeListView, self).get_context_data(**kwargs)
        context['incomes'] = Income.objects.filter(income_type='outcome').select_related('user')
        return context


class IncomeDetailView(TemplateView):
    template_name = 'income_detail.html'

    def get_context_data(self, pk, **kwargs):
        context = super(IncomeDetailView, self).get_context_data(**kwargs)
        income = Income.objects.get(id=pk)
        context['income'] = income
        context['income_product_items'] = IncomeProductItem.objects.filter(income=income)
        context['income_raw_items'] = IncomeRawItem.objects.filter(income=income)
        context['raws'] = Raw.objects.filter(status='active') \
            .annotate(remainder_count=Subquery(WarehouseRaw.objects.filter(raw_id=OuterRef('pk')).values('count')[:1]
        ))
        context['products'] = Product.objects.filter(status='active')
        return context


class IncomeActionView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(IncomeActionView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        post_request = self.request.POST
        user = self.request.user
        action = post_request.get('action', None)
        actions = {
            'create_income': create_income,
            'get_product_weight_and_color_info': get_product_weight_and_color_info,
            'create_income_product_item': create_income_product_item,
            'create_income_raw_item': create_income_raw_item,
            'delete_income_product_item': delete_income_product_item,
            'delete_income_raw_item': delete_income_raw_item,
            'change_income_status': change_income_status,
            'get_remainder_count_product': get_remainder_count_product,
        }
        response = actions[action](post_request, user)
        back_url = response['back_url']
        if action == 'get_product_weight_and_color_info' or action == 'get_remainder_count_product':
            return JsonResponse(response, safe=True)
        return redirect(back_url)
