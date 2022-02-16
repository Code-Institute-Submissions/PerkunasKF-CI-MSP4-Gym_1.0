from django import forms
from .models import OrderUnique


class OrderForm(forms.ModelForm):
    """ Dummy Tag """

    class Meta:
        """ Dummy Tag """

        model = OrderUnique
        fields = ('user_profile', 'email',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """

        super().__init__(*args, **kwargs)
        placeholders = {
            'user_profile': 'User Profile',
            'email': 'Email Address',
        }

        self.fields['user_profile'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'fform'
            self.fields[field].label = False
