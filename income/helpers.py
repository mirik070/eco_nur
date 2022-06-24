from django.db.models import F
from django.http import JsonResponse
from django.urls import reverse

from income.models import Income, IncomeProductItem, IncomeRawItem
from product.models import ProductWeight, ProductColor
from warehouse.models import WarehouseProduct, WarehouseRaw


def create_income(post_request, user):
    warehouse_type = post_request.get('warehouse_type')
    content = post_request.get('content')
    income_type = post_request.get('income_type')
    income = Income.objects.create(warehouse_type=warehouse_type, content=content, user=user, income_type=income_type)
    return dict({'back_url': reverse(post_request.get('back_url', 'income_detail'), kwargs={'pk': income.pk}),
                 'data': ''})


def get_product_weight_and_color_info(post_request, user):
    product_id = post_request.get('product_id')
    results = {'product_weights': [],
               'product_colors': []}
    product_weights = ProductWeight.objects.filter(product_id=product_id)
    product_colors = ProductColor.objects.filter(product_id=product_id)
    for product_weight in product_weights:
        results['product_weights'].append({
            'id': product_weight.id,
            'weight': product_weight.weight,
            'price': product_weight.price,
            'unit': product_weight.product.get_unit_display(),
        })
    for product_color in product_colors:
        results['product_colors'].append({
            'id': product_color.id,
            'color': product_color.color
        })
    return dict({
        'back_url': reverse(post_request.get('back_url', 'income_list')),
        'results': results
    })


def get_remainder_count_product(post_request, user):
    order_id = post_request.get('order_id')
    product_id = post_request.get('product_id')
    product_weight_id = post_request.get('product_weight_id')
    product_color_id = post_request.get('product_color_id')
    try:
        count = WarehouseProduct.objects.get(product_id=product_id, product_weight_id=product_weight_id,
                                             product_color_id=product_color_id).count
    except WarehouseProduct.DoesNotExist:
        count = 0
    results = {
        'count': count
    }
    return dict({
        'back_url': reverse(post_request.get('back_url', 'order_detail'), kwargs={'pk': order_id}),
        'results': results
    })


def create_income_product_item(post_request, user_request):
    income_id = post_request.get('income_id', None)
    product_id = post_request.get('product', None)
    product_weight_id = post_request.get('product_weight', None)
    product_color_id = post_request.get('product_color', None)
    count = post_request.get('count', None)
    price = post_request.get('price', None)
    total = post_request.get('total', None)
    content = post_request.get('content', None)
    IncomeProductItem.objects.create(income_id=income_id,
                                     product_id=product_id,
                                     product_weight_id=product_weight_id,
                                     product_color_id=product_color_id,
                                     count=count,
                                     price=price,
                                     total=total,
                                     content=content)
    return dict({
        'back_url': reverse(post_request.get('back_url', 'income_detail'), kwargs={'pk': income_id}),
        'data': ''
    })


def create_income_raw_item(post_request, user_request):
    income_id = post_request.get('income_id', None)
    raw_id = post_request.get('raw', None)
    count = post_request.get('count', None)
    price = post_request.get('price', None)
    total = post_request.get('total', None)
    content = post_request.get('content', None)
    IncomeRawItem.objects.create(income_id=income_id,
                                 raw_id=raw_id,
                                 count=count,
                                 price=price,
                                 total=total,
                                 content=content)
    return dict({
        'back_url': reverse(post_request.get('back_url', 'income_detail'), kwargs={'pk': income_id}),
        'data': ''
    })


def delete_income_product_item(post_request, user):
    income_id = post_request.get('income_id')
    income_product_item_id = post_request.get('income_product_item_id')
    IncomeProductItem.objects.filter(id=income_product_item_id).delete()
    return dict({
        'back_url': reverse(post_request.get('back_url', 'income_detail'), kwargs={'pk': income_id}),
        'data': ''
    })


def delete_income_raw_item(post_request, user):
    income_id = post_request.get('income_id')
    income_raw_item_id = post_request.get('income_raw_item_id')
    IncomeRawItem.objects.filter(id=income_raw_item_id).delete()
    return dict({
        'back_url': reverse(post_request.get('back_url', 'income_detail'), kwargs={'pk': income_id}),
        'data': ''
    })


def change_income_status(post_request, user):
    status = post_request.get('status', None)
    income_id = post_request.get('income_id', None)
    income = Income.objects.get(id=income_id)
    if status == 'accepted':
        if income.warehouse_type == 'product':
            income_product_items = IncomeProductItem.objects.filter(income_id=income_id)
            for item in income_product_items:
                obj, created = WarehouseProduct.objects.get_or_create(product_id=item.product_id,
                                                                      product_color_id=item.product_color_id,
                                                                      product_weight_id=item.product_weight_id,
                                                                      defaults={'count': item.count})
                if not created:
                    obj.count += item.count
                    obj.save()
        elif income.warehouse_type == 'raw':
            income_raw_items = IncomeRawItem.objects.filter(income_id=income_id)
            print(income_raw_items)
            if income.income_type == 'outcome':
                for item in income_raw_items:
                    WarehouseRaw.objects.filter(raw_id=item.raw_id).update(count=F('count') - item.count)
            else:
                for item in income_raw_items:
                    obj, created = WarehouseRaw.objects.get_or_create(raw_id=item.raw_id,
                                                                      defaults={'count': item.count})
                    if not created:
                        obj.count += item.count
                        obj.save()
    income.status = status
    income.save()
    return dict({
        'back_url': reverse(post_request.get('back_url', 'income_detail'), kwargs={'pk': income_id}),
        'data': ''
    })
