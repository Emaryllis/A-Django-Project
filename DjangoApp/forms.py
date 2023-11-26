from django import forms
from django.contrib.auth.models import User

from DjangoApp.models import UserProfileInfo

def catchBot(value):
    if value:
        raise forms.ValidationError('BOT DETECTED!')

class StarterForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    confirmEmail = forms.EmailField(label='Enter Email Again:')
    text = forms.CharField(widget=forms.Textarea)
    botCatcher = forms.CharField(required=False, widget=forms.HiddenInput,
                                 validators=[catchBot])

    def clean(self):
        allCleanData = super().clean()
        if allCleanData['email'] != allCleanData['confirmEmail']:
            raise forms.ValidationError('Emails do not match!')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        # Only use these fields from User model
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        # Only use these fields from UserProfileInfo model
        fields = ('portfolioSite', 'profilePic')
        # Set form label name
        labels = {
            'portfolioSite': 'Portfolio Website',
            'profilePic': 'Profile Picture'
        }
