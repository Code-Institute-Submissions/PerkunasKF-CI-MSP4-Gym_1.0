from django.shortcuts import render


def inventory(request):
    """ Displays users inventory """

    template = 'user_inventory/inventory.html'
    context = {}

    return render(request, template, context)
