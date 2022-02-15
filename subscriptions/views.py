from django.shortcuts import render, get_object_or_404
from .models import Plan

# Create your views here.


def plans(request):
    """ A view to show subscriptions plans """

    items = Plan.objects.all()

    context = {
        'items': items,
    }
    
    return render(request, 'subscriptions/plans.html', context)


def plan_details(request, item_id):
    """ A view to show specific subscription plan """

    item = get_object_or_404(Plan, pk=item_id)

    context = {
        'item': item,
    }
    
    return render(request, 'subscriptions/plan_details.html', context)
