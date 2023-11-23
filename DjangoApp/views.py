from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    data = {'homeData': 'From views.py!'}
    return render(request, 'home.html', data)

def secondPage(request):
    return HttpResponse("<em>My Second App</em>")

def helpPage(request):
    data = {'helpData': 'The Help Page'}
    return render(request, 'help.html', data)
