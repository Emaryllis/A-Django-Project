from django import forms

from DjangoApp.models import User

def catchBot(value):
    if value:
        raise forms.ValidationError('BOT DETECTED!')

class Form(forms.Form):
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

class NewUserForm(forms.ModelForm):
    # Not required to put first and last name and email in here because they are already provided by the User model
    class Meta:
        model = User
        fields = '__all__'
