from django import forms
from django.contrib.auth.models import User
from .models import Player, profile, stadium


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'age', 'role', 'nationality', 'franchise', 'photo']


class StadiumForm(forms.ModelForm):
    class Meta:
        model = stadium
        fields = ['name', 'location', 'capacity', 'home_team']


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

    # 🔥 MOST IMPORTANT PART
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class ProfileForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['phone_number', 'address', 'profile_picture']
