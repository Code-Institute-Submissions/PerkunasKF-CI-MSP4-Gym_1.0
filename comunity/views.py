from django.shortcuts import (render, redirect, reverse,
                              get_object_or_404)


from profiles.models import UserProfile
from .models import ComunityMessages
from .forms import MessageForm

# Create your views here.


def comunity(request):
    """ 
    Renders comunity page
    """

    title = ComunityMessages.objects.all()
    dates = []
    for date in title:
        dates.insert(0, date.date)

    if request.method == "POST":
        form_data = {
            'username': request.POST['message_username'],
            'title': request.POST['message_title'],
            'message_content': request.POST['message_content'],
        }

        message_form = MessageForm(form_data)
        # saves the message
        if message_form.is_valid():
            message = message_form.save(commit=False)
            message.save()

            # username = get_object_or_404(UserProfile, user=request.user)

            # template = 'comunity/comunity.html'

            # context = {
            #     'title': title,
            #     'username': username,
            # }

            return redirect(reverse('comunity'))
            # return render(request, template, context)
    else:
        # if user is registered poasses user name
        if request.user.is_authenticated:
            username = get_object_or_404(UserProfile, user=request.user)

            template = 'comunity/comunity.html'

            context = {
                'title': title,
                'username': username,
                'dates': dates
            }

            return render(request, template, context)
        else:
            template = 'comunity/comunity.html'

            context = {
                'title': title,
                'dates': dates
            }

            return render(request, template, context)
