from django.shortcuts import render, get_object_or_404

from .models import UserInventory


def user_inventory(request):
    """ Displays users inventory """

    inventory = get_object_or_404(UserInventory, user=request.user)

    template = 'user_inventory/inventory.html'
    context = {
        'inventory': inventory,
    }

    return render(request, template, context)
