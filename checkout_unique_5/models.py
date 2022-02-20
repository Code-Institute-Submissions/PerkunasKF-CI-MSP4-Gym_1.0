import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField

from products.models import Product
from profiles.models import UserProfile


class OrderUnique(models.Model):
    """ Dummy Tag """

    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='orders_unique')
    username = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):
        """ Generate a random, unique order number using UUID """

        return uuid.uuid4().hex.upper()

    # def update_total(self):
    #     """ Update grand total each time a line item is added,
    #     accounting for delivery costs. """

    #     self.order_total = self.lineitems.aggregate('lineitem_total'))[ or 0
    #     self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
    #     self.grand_total = self.order_total + self.delivery_cost
    #     self.save()

    def save(self, *args, **kwargs):
        """ Override the original save method to set the order number
        if it hasn't been set already. """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItemUnique(models.Model):
    """ Dummy Tag """

    order = models.ForeignKey(OrderUnique, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """ Override the original save method to set the lineitem total
        and update the order total. """
        
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'
