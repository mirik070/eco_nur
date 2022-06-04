from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from order.helpers import create_order, create_order_item, delete_order_item, change_order_status
from order.models import Order, OrderItem
from product.models import Product


class OrderCreatedListView(TemplateView):
    template_name = 'order_created_list.html'

    def get_context_data(self, **kwargs):
        context = super(OrderCreatedListView, self).get_context_data(**kwargs)
        context['orders'] = Order.objects.select_related('agent').filter(status='created')
        return context


class OrderPendingListView(TemplateView):
    template_name = 'order_pending_list.html'

    def get_context_data(self, **kwargs):
        context = super(OrderPendingListView, self).get_context_data(**kwargs)
        context['orders'] = Order.objects.select_related('agent').filter(status='pending')
        return context


class OrderListView(TemplateView):
    template_name = 'order_list.html'

    def get_context_data(self, **kwargs):
        context = super(OrderListView, self).get_context_data(**kwargs)
        context['orders'] = Order.objects.select_related('agent').exclude(status='created')
        return context


class OrderDetailView(TemplateView):
    template_name = 'order_detail.html'

    def get_context_data(self, pk, **kwargs):
        context = super(OrderDetailView, self).get_context_data(**kwargs)
        order = Order.objects.get(id=pk)
        context['order'] = order
        context['order_items'] = OrderItem.objects.filter(order_id=pk)
        context['products'] = Product.objects.filter(status='active')
        if order.status == 'created':
            context['back_url'] = 'order_created_list'
        elif order.status == 'pending':
            context['back_url'] = 'order_pending_list'
        else:
            context['back_url'] = 'order_list'
        return context


class OrderActionView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(OrderActionView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        post_request = self.request.POST
        file_request = self.request.FILES
        user = self.request.user
        action = self.request.POST.get('action', None)
        print(action)
        actions = {
            'create_order': create_order,
            'create_order_item': create_order_item,
            'delete_order_item': delete_order_item,
            'change_order_status': change_order_status,
        }
        response = actions[action](post_request, file_request, user)
        back_url = response['back_url']
        return redirect(back_url)
