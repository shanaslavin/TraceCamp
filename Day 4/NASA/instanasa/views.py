from django.shortcuts import render
from instanasa.models import instanasa
import requests
from django.views.generic import TemplateView, CreateView, DetailView, ListView, UpdateView, DeleteView
from instanasa.forms.forms import InstanasaForm
from django.urls import reverse_lazy

# Create your views here.

class date_selecter(TemplateView):
    template_name= "date_selecter.html"

class instanasaCreateView(CreateView):
    
    def __init__(self):
        super().__init__()
        self.image_url = ""

    form_class = InstanasaForm
    template_name = 'instanasa/instanasa_form.html'

    def get_initial(self, **kwargs):
        initial_form = super().get_initial(**kwargs)
        initial_form['date'] = self.request.GET.get("date", "")
        initial_form['url'] = self.image_url
        return initial_form
    
    def get(self, request):
        date = self.request.GET.get("date", '2017-01-01')
        api_key = "oMrH77hL0IcYFpEAYw6HpzxULiro2VX2jGy9CIMV"
        r = requests.get(f'https://api.nasa.gov/planetary/apod?date={date}&api_key={api_key}')
        url = r.json()['url']
        self.image_url = url
        get_response = super().get(request)
        return get_response
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url'] = self.image_url
        return context
    


class instanasaDetailView(DetailView):
    model = instanasa

class instanasaListView(ListView):
    model = instanasa

class instanasaUpdateView(UpdateView):
    model = instanasa
    fields = ['comments', 'rating', 'favorite']

class instanasaDeleteView(DeleteView):
    model = instanasa
    success_url = reverse_lazy('list_comments')

