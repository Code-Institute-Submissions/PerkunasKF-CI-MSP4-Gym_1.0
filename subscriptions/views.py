from django.shortcuts import render, get_object_or_404
from .models import Plan

# Create your views here.


from django.shortcuts import render

# Create your views here.

def plans(request):
    """ A view to show subscriptions plans """

    plans = Plan.objects.all()

    context = {
        'plans': plans,
    }
    
    return render(request, 'subscriptions/plans.html', context)


def plan_details(request, plan_id):
    """ A view to show specific subscription plan """

    plan = get_object_or_404(Plan, pk=plan_id)

    context = {
        'plan': plan,
    }
    
    return render(request, 'subscriptions/plan_details.html', context)