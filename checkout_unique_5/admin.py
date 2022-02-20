from django.contrib import admin
from .models import OrderUnique, OrderLineItemUnique

# Register your models here.


class OrderLineItemAdminInlineUnique(admin.TabularInline):
    """ Dummy Tag """

    model = OrderLineItemUnique
    readonly_fields = ('lineitem_total',)


class OrderAdminUnique(admin.ModelAdmin):
    """ Dummy Tag """
    
    inlines = (OrderLineItemAdminInlineUnique,)

    readonly_fields = ('order_number', 'date', 'order_total',
                       'stripe_pid')

    fields = ('order_number', 'user_profile', 'date', 'username',
              'email', 'order_total', 'stripe_pid')

    list_display = ('order_number', 'date', 'username',
                    'order_total',)

    ordering = ('-date',)

admin.site.register(OrderUnique, OrderAdminUnique)
