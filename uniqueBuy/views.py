from django.shortcuts import render

# from subscriptions.models import Plan

# Create your views here.


def view_unique(request):
    """ A view that renders the unique item to buy """

    return render(request, 'uniqueBuy/unique.html')