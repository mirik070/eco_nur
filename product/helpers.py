from django.urls import reverse

from product.models import Product, ProductWeight, ProductColor, ProductCategory


def strip_and_capitalize_list(arr: list):
    return list(filter(bool, map(lambda x: x.strip().capitalize(), arr)))


def create_product_category(post_request, user):
    title = post_request.get('title')
    ProductCategory.objects.create(title=title)
    return dict({'back_url': post_request.get('back_url', 'product_category_list'),
                 'data': ''})


def update_product_category(post_request, user):
    product_category_id = post_request.get('product_category_id')
    title = post_request.get('title')
    status = post_request.get('status')
    ProductCategory.objects.filter(id=product_category_id).update(title=title, status=status)
    return dict({'back_url': post_request.get('back_url', 'product_category_list'),
                 'data': ''})


def create_product(post_request, user):
    category_id = post_request.get('category_id')
    title = post_request.get('title')
    unit = post_request.get('unit')
    colors = strip_and_capitalize_list(post_request.getlist('color'))
    product = Product.objects.create(category_id=category_id, title=title, unit=unit)
    ProductColor.objects.bulk_create([
        ProductColor(
            color=color,
            product=product
        ) for color in colors
    ])
    return dict({'back_url': reverse(post_request.get('back_url', 'product_list'), kwargs={'pk': category_id}),
                 'data': ''})


def update_product(post_request, user):
    category_id = post_request.get('category_id')
    unit = post_request.get('unit')
    title = post_request.get('title')
    colors = strip_and_capitalize_list(post_request.getlist('color'))
    price = post_request.get('price')
    cost_price = post_request.get('cost_price')
    product_id = post_request.get('product_id')
    product = Product.objects.get(id=product_id)
    colors_list = product.productcolor_set.all()
    for old_color in colors_list:
        if old_color.color not in colors:
            old_color.delete()
    product.title = title
    product.price = price
    product.unit = unit
    product.cost_price = cost_price
    colors_names = list(map(lambda x: x.color, colors_list))
    for color in colors:
        if color not in colors_names:
            product.productcolor_set.create(color=color)
    product.save()
    return dict({'back_url': reverse(post_request.get('back_url', 'product_list'), kwargs={'pk': category_id}),
                 'data': ''})


def create_product_weight(post_request, user):
    product_id = post_request.get('product_id')
    weight = post_request.get('weight')
    price = post_request.get('price')
    ProductWeight.objects.create(weight=weight, price=price, product_id=product_id)
    return dict({'back_url': reverse(post_request.get('back_url', 'product_detail'), kwargs={'pk': product_id}),
                 'data': ''})


def delete_product_weight(post_request, user):
    product_id = post_request.get('product_id')
    product_weight_id = post_request.get('product_weight_id')
    ProductWeight.objects.filter(id=product_weight_id).delete()
    return dict({'back_url': reverse(post_request.get('back_url', 'product_detail'), kwargs={'pk': product_id}),
                 'data': ''})