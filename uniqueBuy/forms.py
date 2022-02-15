from django import forms
from .models import OrderUnique


class OrderFormUnique(forms.ModelForm):
    """ Dummy tag """
    class Meta:
        """ Dummy tag """
        model = OrderUnique
        fields = ('user_profile', 'email',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'user_profile': 'Full Name',
            'email': 'Email Address',
        }

        self.fields['user_profile'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
