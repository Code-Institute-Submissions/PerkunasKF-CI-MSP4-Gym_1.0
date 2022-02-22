from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from checkout_unique_5.models import OrderUnique

from products.models import Product
from .models import UserInventory
from .forms import UserInventoryForm


def user_inventory(request):
    """ Displays users inventory """

    if request.user.is_authenticated:
        inventory = get_object_or_404(UserInventory, user=request.user)

        username = request.user
        orders = inventory.orders_unique.all()

        template = 'user_inventory/inventory.html'
        context = {
            'orders': orders,
            'username': username,
        }

        return render(request, template, context)
    else:
        return render(request, 'home/index.html')


def order_history_unique(request, order):
    """
    Gets order numbers checkout_unique app
    """

    order = get_object_or_404(OrderUnique, order_number=order)

    for item in order.lineitems_unique.all():
        product_data = item.product.id
    product = get_object_or_404(Product, id=product_data)

    messages.info(request, (
        f'This is a past confirmatio for order number {order.order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout_unique_5/checkout_success.html'
    context = {
        'order': order,
        'product': product,
        'from_inventory': True,
    }

    return render(request, template, context)
