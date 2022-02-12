from django.shortcuts import render
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