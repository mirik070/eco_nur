from warehouse.models import Raw


def create_raw(post_request, user):
    title = post_request.get('title')
    unit = post_request.get('unit')
    price = post_request.get('price')
    Raw.objects.create(title=title, unit=unit, price=price)
    return dict({'back_url': post_request.get('back_url', 'raw_list'),
                 'data': ''})


def update_raw(post_request, user):
    raw_id = post_request.get('raw_id')
    title = post_request.get('title')
    price = post_request.get('price')
    unit = post_request.get('unit')
    status = post_request.get('status')
    Raw.objects.filter(id=raw_id).update(title=title, unit=unit, status=status, price=price)
    return dict({'back_url': post_request.get('back_url', 'raw_list'),
                 'data': ''})
