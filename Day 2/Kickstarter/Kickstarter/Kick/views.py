from django.shortcuts import render
from django.http import HttpResponse
from Kick.models import Kickstarter_camp
from django.core import serializers

def kick_view(request, kick_id):
    
    html = Kickstarter_camp.objects.filter(
        id=kick_id
    )
    data = serializers.serialize("json", html)
    return HttpResponse(data)


# Create your views here.

