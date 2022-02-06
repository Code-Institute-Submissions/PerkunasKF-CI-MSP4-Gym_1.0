from django import forms
from .models import Product, Category


class ProductForm(form.ModelForm):
    """Dummy tag"""

    class Meta:
        """Dummy Tag"""
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        supper().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_name = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'transparent-bbtn'