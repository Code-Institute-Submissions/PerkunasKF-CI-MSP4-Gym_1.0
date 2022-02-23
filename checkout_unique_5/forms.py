from django import forms
from .models import OrderUnique


class OrderFormUnique(forms.ModelForm):
    """ Dummy Tag """

    class Meta:
        """ Dummy Tag """

        model = OrderUnique
        fields = ('username', 'email')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        
        super().__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'fform'
            self.fields[field].widget.attrs['readonly'] = True
