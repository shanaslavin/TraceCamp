from django import forms
from findpet.models import pet

class descriptionForm(forms.ModelForm):
    class Meta:
        model = pet
        fields = ['description', 'lng', 'lat', 'image']


class ImageFileForm(forms.Form):
    image = forms.FileField()


