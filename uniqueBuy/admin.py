from django.contrib import admin
from .models import OrderUnique

# Register your models here.


class OrderAdminUnique(admin.ModelAdmin):
    """ Dummy tag """

    readonly_fields = ('order_number', 'date', 'order_total',
                       'stripe_pid',)

    fields = ('order_number', 'user_profile', 'date',
              'email', 'order_total', 'stripe_pid',)

    list_display = ('order_number', 'date', 'user_profile',
                    'order_total',)

    ordering = ('-date',)


admin.site.register(OrderUnique, OrderAdminUnique)