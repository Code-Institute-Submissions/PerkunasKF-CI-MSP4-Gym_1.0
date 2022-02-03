from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instace, created, **kwargs):
    """
    Update order total on lineitem updat/creat
    """
    instance.order.updat_total()


@receiver(post_delete, sender=OrderLineItem)
def update_on_save(sender, instace, **kwargs):
    """
    Update order total on lineitem delete
    """
    instance.order.updat_total()