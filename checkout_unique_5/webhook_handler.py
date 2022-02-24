from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import OrderUnique, OrderLineItemUnique
from products.models import Product
from user_inventory.models import UserInventory

import json
import time


class StripeWHHandlerUnique:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """Send the user a confirmation email"""
        cust_email = order.email
        subject = render_to_string(
            'checkout_unique_5/confirmation_emails/confirmation_email_subject_unique.txt',
            {'order': order})
        body = render_to_string(
            'checkout_unique_5/confirmation_emails/confirmation_email_body_unique.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})
        
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )        

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """

        intent = event.data.object
        pid = intent.id
        product = intent.metadata.product
        item = Product.objects.get(id=product)

        billing_details = intent.charges.data[0].billing_details
        order_total = round(item.price / 100, 2)

        # # Update profile information if save_info was checked
        profile = None
        username = intent.metadata.username
        profile = UserInventory.objects.get(user__username=username)

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = OrderUnique.objects.get(
                    username__iexact=billing_details.name,
                    user_inventory__iexact=profile,
                    email__iexact=billing_details.email,
                    order_total=order_total,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except OrderUnique.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            order = None
            try:
                order = OrderUnique.objects.create(
                    username=billing_details.name,
                    user_inventory=profile,
                    email=billing_details.email,
                    stripe_pid=pid,
                    order_total=item.price,
                )
                
                order_line_item = OrderLineItemUnique(
                    order=order,
                    product=item,
                    lineitem_total=item.price,
                )
                order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)