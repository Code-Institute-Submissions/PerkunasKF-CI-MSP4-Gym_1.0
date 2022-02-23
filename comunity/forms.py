from django import forms
from .models import ComunityMessages


class MessageForm(forms.ModelForm):
    """ Dummy Tag """

    class Meta:
        """ Dummy Tag """

        model = ComunityMessages
        fields = ('username', 'title', 'message_content')
