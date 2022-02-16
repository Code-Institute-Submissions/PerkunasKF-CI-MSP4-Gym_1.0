from django.contrib import admin
from .models import OrderUnique, OrderLineItemUnique

# Register your models here.


class OrderLineItemAdminInlineUnique(admin.TabularInline):
    """ Model for sectio in admin tools to ajust unique orders """

    model = OrderLineItemUnique
    readonly_fields = ('lineitem_total',)


class OrderAdminUnique(admin.ModelAdmin):
    """ Model to view unique orders in admin tools """

    inlines = (OrderLineItemAdminInlineUnique,)

    readonly_fields = ('order_number', 'date',
                       'order_total', 'stripe_pid', 'username',
                       'email',)

    fields = ('order_number', 'user_profile', 'date',
              'email', 'order_total', 'stripe_pid')

    list_display = ('order_number', 'date', 'user_profile',
                    'order_total',)

    ordering = ('-date',)

admin.site.register(OrderUnique, OrderAdminUnique)
