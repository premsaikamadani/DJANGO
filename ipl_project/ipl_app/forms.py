from django import forms
from django.contrib.auth.models import User
from .models import Player, profile, stadium

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        #fields = '__all__'
        fields = ['name', 'age', 'role', 'nationality', 'franchise', 'photo']


class stadiumForm(forms.ModelForm):
    class Meta:
       model = stadium
       fields = ['name', 'location', 'capacity', 'home_team']


class userRegistrationForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']


class profileForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['phone_number', 'address', 'profile_picture']