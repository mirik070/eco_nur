from django.db.models import F
from django.urls import reverse

from order.models import Order, OrderItem
from warehouse.models import WarehouseProduct


def create_order(post_request, file_request, user):
    address = post_request.get('address')
    shop_photo = file_request.get('shop_photo')
    shop_name = post_request.get('shop_name')
    phone = post_request.get('phone')
    payment_type = post_request.get('payment_type')
    order = Order.objects.create(agent=user,
                                 address=address,
                                 shop_photo=shop_photo,
                                 shop_name=shop_name,
                                 phone=phone,
                                 payment_type=payment_type)
    return dict({'back_url': reverse(post_request.get('back_url', 'order_detail'), kwargs={'pk': order.id}),
                 'data': ''})


def create_order_item(post_request, file_request, user):
    order_id = post_request.get('order_id', None)
    product_id = post_request.get('product', None)
    product_weight_id = post_request.get('product_weight', None)
    product_color_id = post_request.get('product_color', None)
    count = post_request.get('count', None)
    content = post_request.get('content', None)
    OrderItem.objects.create(order_id=order_id,
                             product_id=product_id,
                             product_weight_id=product_weight_id,
                             product_color_id=product_color_id,
                             count=count,
                             content=content)
    return dict({
        'back_url': reverse(post_request.get('back_url', 'order_detail'), kwargs={'pk': order_id}),
        'data': ''
    })


def delete_order_item(post_request, file_request, user):
    order_id = post_request.get('order_id', None)
    order_item_id = post_request.get('order_item_id')
    OrderItem.objects.filter(id=order_item_id).delete()
    return dict({
        'back_url': reverse(post_request.get('back_url', 'order_detail'), kwargs={'pk': order_id}),
        'data': ''
    })


def change_order_status(post_request, file_request, user):
    status = post_request.get('status', None)
    order_id = post_request.get('order_id', None)
    order = Order.objects.get(id=order_id)
    if status == 'sent':
        order_items = OrderItem.objects.filter(order_id=order_id)
        for item in order_items:
            WarehouseProduct.objects.filter(product_id=item.product_id,
                                            product_color_id=item.product_color_id,
                                            product_weight_id=item.product_weight_id)\
                .update(count=F('count') - item.count)
    order.status = status
    order.save()
    return dict({
        'back_url': reverse(post_request.get('back_url', 'order_detail'), kwargs={'pk': order_id}),
        'data': ''
    })
