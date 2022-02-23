from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from profiles.models import UserProfile
from .models import ComunityMessages

# Create your views here.


def comunity(request):
    """ 
    Renders comunity page
    """

    title = ComunityMessages.objects.all()
    data = []

    user = 'Anonymous'

    if request.user.is_authenticated:
        user = get_object_or_404(UserProfile, user=request.user)

    template = 'comunity/comunity.html'

    context = {
        'title': title,
    }

    return render(request, template, context)
