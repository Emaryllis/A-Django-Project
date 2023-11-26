from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from DjangoApp import forms
from DjangoApp.forms import UserForm, UserProfileInfoForm
from DjangoApp.models import AccessRecord

def Home(request):
    homeData = {'homeData': 'From views.py!'}
    return render(request, 'client/home.html', homeData)

def AccessRecords(request):
    pageList = AccessRecord.objects.order_by('dateAccessed')
    data = {'accessRecordsData': pageList}
    return render(request, 'client/accessRecords.html', data)

def Form(request):
    form = forms.StarterForm()
    if request.method == 'POST':
        form = forms.StarterForm(request.POST)
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

@login_required
def Dashboard(request):
    return HttpResponse("You have successfully logged, therefore you are able to see the dashboard!")

@login_required
def userLogout(request):
    logout(request)
    return redirect(reverse('DjangoApp:home'))

def Register(request):
    registered = False
    if request.method != 'POST':
        userForm = UserForm()
        profileForm = UserProfileInfoForm()
    else:
        # Display both forms
        userForm = UserForm(data=request.POST)
        profileForm = UserProfileInfoForm(data=request.POST)

        # Check to see both forms are valid
        if userForm.is_valid() and profileForm.is_valid():

            # User form algorithm
            user = userForm.save()  # Save User Form to db
            user.set_password(user.password)  # Hash password
            user.save()  # Update with hashed password

            # Profile form algorithm
            profile = profileForm.save(commit=False)  # Not committed since need to upload profilePic
            profile.user = user  # Sets UserProfileInfo.user to the user model
            if 'profilePic' in request.FILES:  # Check if they provided a profile picture
                profile.profilePic = request.FILES['profilePic']
            profile.save()  # Update with optional profilePic

            registered = True  # Mark registration as successful
        else:
            print(userForm.errors, profileForm.errors)  # Print error if form was invalid

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request, 'client/register.html',
                  {'userForm': userForm,
                   'profileForm': profileForm,
                   'registered': registered})

def userLogin(request):
    if request.method != 'POST':
        return render(request, 'client/login.html')

    # Get username and password
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)

    # If we have a user
    if not user:
        print("Login failed: Username: %s. Password: %s" % username, password)
        return render(request, 'client/login.html', {'error': 'Invalid login details supplied.'})
    elif not user.is_active:
        return render(request, 'client/login.html', {'error': 'Your account is inactive.'})
    else:
        login(request, user)
        return redirect(reverse('DjangoApp:dashboard'))
