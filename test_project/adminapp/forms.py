from mainapp.models import Product
from django import forms


class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for fieldname, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'
                field.help_text = ''