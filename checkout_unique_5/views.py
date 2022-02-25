from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

import stripe

from products.models import Product
from profiles.models import UserProfile
from user_inventory.models import UserInventory
from .forms import OrderFormUnique
from .models import OrderUnique, OrderLineItemUnique


@require_POST
def cache_checkout_data_unique(request):
    """ Adding values to checkout data """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY

        stripe.PaymentIntent.modify(pid, metadata={
            'username': request.user,
            'product': request.POST.get('product_data'),
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout_unique(request, item_id):
    """ Dummy Tag """
    
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    # Getting basik values for checkout
    item = get_object_or_404(Product, pk=item_id)
    total = item.price
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )
    # Submits form information after confirming purches
    if request.method == 'POST':
        form_data = {
            'username': request.POST['username'],
            'email': request.POST['email'],
        }
        
        order_form = OrderFormUnique(form_data)
        # Checks is form is valid
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret_unique').split('_secret_unique')[0]
            order.stripe_pid = pid
            order.order_total = item.price
            order.save()
            product = Product.objects.get(id=item_id)
            order_line_item = OrderLineItemUnique(
                order=order,
                product=product,
            )
            order_line_item.save()
            return redirect(reverse('checkout_success_unique', args=[order.order_number, product.id]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        # Checks if user is registered
        if request.user.is_authenticated:
            inventory = get_object_or_404(UserInventory, user=request.user)
            username = request.user
            email = username.email
            orders = inventory.orders_unique.all()
            inventory_products = []

            # Checks if user hase any unique items in inventory
            # If inventory is empty first itme is put to user inventory
            # without charging
            for order in orders:
                for item in order.lineitems_unique.all():
                    inventory_products.insert(0, item.product.id)
            if not inventory_products:
                form_data = {
                    'username': username,
                    'email': email,
                }
                
                order_form = OrderFormUnique(form_data)
                if order_form.is_valid():
                    order = order_form.save(commit=False)
                    order.order_total = 0
                    order.save()
                    product = Product.objects.get(id=item_id)
                    order_line_item = OrderLineItemUnique(
                        order=order,
                        product=product,
                    )
                    order_line_item.save()
                    
                    return redirect(reverse('checkout_success_unique', args=[order.order_number, product.id]))
            # User is charged if user inventory has atleas one itme
            else:
                item = get_object_or_404(Product, pk=item_id)
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderFormUnique(initial={
                    'username': profile.user.username,
                    'email': profile.user.email,
                })

                template = 'checkout_unique_5/checkout_unique.html'
                context = {
                    'item': item,
                    'order_form': order_form,
                    'stripe_public_key': stripe_public_key,
                    'client_secret': intent.client_secret,
                }
            return render(request, template, context)
        else:
            messages.error(request, 'Only registered users can purches this item')
            return redirect(reverse('product_details', args=[item_id]))


def checkout_success_unique(request, order_number, product_id):
    """
    Handle successful checkouts
    """

    order = get_object_or_404(OrderUnique, order_number=order_number)
    product = get_object_or_404(Product, id=product_id)

    if request.user.is_authenticated:
        profile = UserInventory.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_inventory = profile
        order.save()

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    template = 'checkout_unique_5/checkout_success.html'
    context = {
        'order': order,
        'product': product,
    }

    return render(request, template, context)
