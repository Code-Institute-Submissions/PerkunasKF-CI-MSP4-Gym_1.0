from django.contrib import admin
from .models import Plan

# Register your models here.


class PlanAdmin(admin.ModelAdmin):
    """ Dummy Tag """
    list_display = (
        'name',
        'line1',
        'line2',
        'line3',
        'price',
        'image',
    )


admin.site.register(Plan, PlanAdmin)