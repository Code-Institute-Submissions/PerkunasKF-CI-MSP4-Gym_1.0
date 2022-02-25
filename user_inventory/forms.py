from django import forms
from .models import UserInventory


class UserInventoryForm(forms.ModelForm):
    """Dummy tag"""

    class Meta:
        """Dummy tag"""

        model = UserInventory
        fields = ('username',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'fform'
            self.fields[field].widget.attrs['readonly'] = True
