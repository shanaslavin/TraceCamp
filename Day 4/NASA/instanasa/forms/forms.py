from django.forms import ModelForm, HiddenInput
from instanasa.models import instanasa

class InstanasaForm(ModelForm):
    class Meta:
        model = instanasa
        fields = ['comments', 'rating', 'favorite', 'date', 'url']

        widgets = {
            'url' : HiddenInput,
            'date' : HiddenInput
        }

