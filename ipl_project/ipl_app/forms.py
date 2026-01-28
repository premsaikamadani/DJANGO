from django import forms
from .models import Player, stadium

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        #fields = '__all__'
        fields = ['name', 'age', 'role', 'nationality', 'franchise', 'photo']


class stadiumForm(forms.ModelForm):
    class Meta:
       model = stadium
       fields = ['name', 'location', 'capacity', 'home_team']