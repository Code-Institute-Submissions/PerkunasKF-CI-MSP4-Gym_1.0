from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

import stripe
import json

from products.models import Product
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from .forms import OrderFormUnique
from .models import OrderUnique, OrderLineItemUnique


# @require_POST
# def cache_checkout_data(request):
#     """ Dummy Tag """
#     try:
#         pid = request.POST.get('client_secret').split('_secret')[0]
#         stripe.api_key = settings.STRIPE_SECRET_KEY
#         stripe.PaymentIntent.modify(pid, metadata={
#             'bag': json.dumps(request.session.get('bag', {})),
#             'save_info': request.POST.get('save_info'),
#             'username': request.user,
#         })
#         return HttpResponse(status=200)
#     except Exception as e:
#         messages.error(request, 'Sorry, your payment cannot be \
#             processed right now. Please try again later.')
#         return HttpResponse(content=e, status=400)


def checkout_unique(request, item_id):
    """ Dummy Tag """

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    item = get_object_or_404(Product, pk=item_id)

    item_price = item.price
    stripe_price = round(item_price * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_price,
        currency=settings.STRIPE_CURRENCY,
    )
    print('---------Test------------')
    print(intent)

    if request.user.is_authenticated:
        if request.method == 'POST':
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderFormUnique(initial={
                    'username': profile.user.get_username(),
                    'email': profile.user.email,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderFormUnique()
        else:
            if not item:
                messages.error(request, "There's nothing to add to your Inventory")
                return redirect(reverse('product_detail', args=[item_id]))
            
            item_price = item.price
            stripe_price = round(item_price * 100)
            stripe.api_key = stripe_secret_key
            intent = stripe.PaymentIntent.create(
                amount=stripe_price,
                currency=settings.STRIPE_CURRENCY,
            )
            print('---------Test------------')
            print(intent)

        if not stripe_public_key:
            messages.warning(request, 'Stripe public key is missing. \
                Did you forget to set it in your environment?')

        template = 'checkout_unique/checkout_unique.html'
        context = {
            'item': item,
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }
    else:
        messages.error(request, "Only registered users can purches this item")
        return redirect(reverse('product_detail', args=[item_id]))

    return render(request, template, context)


# def checkout_success(request, order_number):
#     """
#     Handle successful checkouts
#     """
#     save_info = request.session.get('save_info')
#     order = get_object_or_404(Order, order_number=order_number)

#     if request.user.is_authenticated:
#         profile = UserProfile.objects.get(user=request.user)
#         # Attach the user's profile to the order
#         order.user_profile = profile
#         order.save()

#         # Save the user's info
#         if save_info:
#             profile_data = {
#                 'default_phone_number': order.phone_number,
#                 'default_country': order.country,
#                 'default_postcode': order.postcode,
#                 'default_town_or_city': order.town_or_city,
#                 'default_street_address1': order.street_address1,
#                 'default_street_address2': order.street_address2,
#                 'default_county': order.county,
#             }
#             user_profile_form = UserProfileForm(profile_data, instance=profile)
#             if user_profile_form.is_valid():
#                 user_profile_form.save()

#     messages.success(request, f'Order successfully processed! \
#         Your order number is {order_number}. A confirmation \
#         email will be sent to {order.email}.')

#     if 'bag' in request.session:
#         del request.session['bag']

#     template = 'checkout/checkout_success.html'
#     context = {
#         'order': order,
#     }

#     return render(request, template, context)
