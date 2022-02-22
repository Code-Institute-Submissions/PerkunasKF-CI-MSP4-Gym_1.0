from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from checkout_unique_5.models import OrderUnique

from products.models import Product
from .models import UserInventory
from .forms import UserInventoryForm


def user_inventory(request):
    """ Displays users inventory """

    inventory = get_object_or_404(UserInventory, user=request.user)

    form_data = {
        'username': request.user,
    }

    form = UserInventoryForm(form_data)
    orders = inventory.orders_unique.all()

    template = 'user_inventory/inventory.html'
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)


def order_history_unique(request, order):
    """
    Gets order numbers checkout_unique app
    """

    print('------ Testas -----------')
    print(order)
    print('-------------------------')  

    order = get_object_or_404(OrderUnique, order_number=order)

    print('------ Testas -----------')
    for item in order.lineitems_unique.all():
        product_data = item.product.id
        print(product_data)
    product = get_object_or_404(Product, id=product_data)
    print(product)
    print('-------------------------')    

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
