from django.shortcuts import render
import requests
from django.views.generic import CreateView, DetailView, UpdateView, ListView, DeleteView, TemplateView
from findpet.forms.forms import descriptionForm
from findpet.models import pet
from django.urls import reverse_lazy


# Create your views here.

class descriptionCreateView(CreateView):
    
    model = pet

    form_class = descriptionForm
    template_name = 'findpet/pet_form.html'


    def get_initial(self, **kwargs):
        initial_form = super().get_initial(**kwargs)
        api_key = "AIzaSyDxEUuE6E8t1bDDtLwRCnFST5juA96nCbU"
        response = requests.post(f'https://www.googleapis.com/geolocation/v1/geolocate?key={api_key}').json()
        self.lng = response['location']['lng']
        longitude = self.lng
        self.lat = response['location']['lat']
        latitude = self.lat
        initial_form['lng'] = float("%.6f" % longitude)
        initial_form['lat'] = float("%.6f" % latitude)
        return initial_form

class descriptionDetailView(DetailView):
    model = pet

class descriptionListView(ListView):
    model = pet
    
class descriptionUpdateView(UpdateView):
    model = pet
    fields = ['description', 'lng', 'lat']
    
class descriptionDeleteView(DeleteView):
    model = pet
    success_url = reverse_lazy('list_view')

class map(TemplateView):
    model = pet
    template_name = 'map.html'

