from django.shortcuts import render, get_object_or_404

from subscriptions.models import Plan
from products.models import Product

# Create your views here.


def unique_buy(request, item_id):
    """ A view that renders the unique item to buy """

    item = get_object_or_404(Plan, pk=item_id)

    print('--------- Test ---------')
    print(item)
    print('------------------------')

    context = {
        'item': item,
    }

    return render(request, 'uniqueBuy/unique_buy.html', context)
