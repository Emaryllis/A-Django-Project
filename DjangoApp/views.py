from django.http import HttpResponseRedirect
from django.shortcuts import render

from DjangoApp import forms
from DjangoApp.models import AccessRecord, User

def Home(request):
    homeData = {'homeData': 'From views.py!'}
    return render(request, 'client/home.html', homeData)

def AccessRecords(request):
    pageList = AccessRecord.objects.order_by('dateAccessed')
    data = {'accessRecordsData': pageList}
    return render(request, 'client/accessRecords.html', data)

def UserList(request):
    userList = User.objects.order_by('firstName')
    data = {'usersData': userList}
    return render(request, 'client/users.html', data)

def Form(request):
    form = forms.Form()
    if request.method == 'POST':
        form = forms.Form(request.POST)
        if form.is_valid():
            print("VALIDATION SUCCESS!")
            print("Name: " + form.cleaned_data['name'])
            print("Email: " + form.cleaned_data['email'])
            print("Text: " + form.cleaned_data['text'])
        # Check for bots
        elif 'botCatcher' in form.errors.keys() and form.errors['botCatcher'].as_text() == 'BOT DETECTED!':
            print("BOT DETECTED!")
            # It doesn't blacklist them its just more of a scaring tactic lol
            return render(request, 'client/formPage.html', {'botCatcher': 'You have been blacklisted.'})
    return render(request, 'client/formPage.html', {'formDisplay': form})

def Register(request):
    form = forms.NewUserForm()
    if request.method == 'POST':
        form = forms.NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/')  # Redirect to home page
        else:
            print("ERROR: INVALID FORM DATA")
    return render(request, 'client/newUser.html', {'formDisplay': form})
