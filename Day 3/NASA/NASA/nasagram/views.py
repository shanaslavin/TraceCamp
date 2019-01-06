from django.shortcuts import render
import requests
from django.shortcuts import redirect
from nasagram.models import nasa_models
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def date_selecter(request):
    return render(request, 'date_selecter.html')
    

def make_comment(request):
    if(request.method == "GET"):
        api_key = "oMrH77hL0IcYFpEAYw6HpzxULiro2VX2jGy9CIMV"

        date = request.GET.get("date")

        r = requests.get(f'https://api.nasa.gov/planetary/apod?date={date}&api_key={api_key}')
        url = r.json()["url"]

        return render(request, 'make_comment.html', {'nasa_img' : url, 'date' : date})
    elif(request.method == "POST"):
        comment_details = nasa_models.objects.create(
            comment = request.POST.get('comment', ''),
            date = datetime.strptime(request.POST.get('date', '2018-01-01'), '%Y-%m-%d').date(),
            rating = request.POST.get('rating', 0),
            favorite = request.POST.get('favorite', False) == "on",
            url = request.POST.get('url', '')
        )
        return redirect(f'/nasa/comment_details/{comment_details.id}')


def comment_details(request, id):
    comment_details = nasa_models.objects.get(id = id)
    return render(request, 'comment_details.html', {"comment_details" : comment_details})


def list_comments(request):
    comments = nasa_models.objects.all()
    return render(request, 'list_comments.html', {'comments' : comments})

