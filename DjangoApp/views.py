from django.http import HttpResponse
from django.shortcuts import render

from DjangoApp.models import AccessRecord, User

# Create your views here.
def home(request):
    data = {'homeData': 'From views.py!'}
    return render(request, 'home.html', data)

def secondPage(request):
    return HttpResponse("<em>My Second App</em>")

def helpPage(request):
    data = {'helpData': 'The Help Page'}
    return render(request, 'help.html', data)

def accessRecords(request):
    webpages_list = AccessRecord.objects.order_by('dateAccessed')
    data = {'accessRecordsData': webpages_list}
    return render(request, 'accessRecords.html', data)

def users(request):
    user_list = User.objects.order_by('firstName')
    data = {'usersData': user_list}
    return render(request, 'users.html', data)
