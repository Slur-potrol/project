from django.shortcuts import render
from products.models import *

def panel_view(request):
    products_images = ProductImage.objects.filter(is_active = True, is_main = True)
    return render(request, 'panel.html', locals())


def product(request, product_id):
    product = Product.objects.get(id=product_id)


    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)


    return render(request, 'product.html', locals())