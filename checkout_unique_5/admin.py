from django.contrib import admin
from .models import OrderUnique, OrderLineItemUnique

# Register your models here.


class OrderLineItemAdminInlineUnique(admin.TabularInline):
    """ Class to show items in unique products admin view """

    model = OrderLineItemUnique
    readonly_fields = ('lineitem_total',)


class OrderAdminUnique(admin.ModelAdmin):
    """ Class to show order information for unique checkouts """
    
    inlines = (OrderLineItemAdminInlineUnique,)

    readonly_fields = ('order_number', 'date', 'order_total',
                       'stripe_pid')

    fields = ('order_number', 'user_inventory', 'date', 'username',
              'email', 'order_total', 'stripe_pid')

    list_display = ('order_number', 'date', 'username',
                    'order_total',)

    ordering = ('-date',)

admin.site.register(OrderUnique, OrderAdminUnique)
