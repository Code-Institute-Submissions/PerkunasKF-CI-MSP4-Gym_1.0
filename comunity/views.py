from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse

from .models import ComunityMessages

# Create your views here.


def comunity(request):
    """ 
    Renders comunity page
    """

    return render(request, 'comunity/comunity.html')