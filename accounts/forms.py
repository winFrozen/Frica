from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Parol",
                               widget=forms.PasswordInput)
    password_2 = forms.CharField(label="Parolni takrorlang",
                                 widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']
    def clean_password2(self):
        data = self.cleaned_data
        if data["password"] != data["password2"]:
            raise forms.ValidationError("Parollar bir xil bo'lish zarur !")


class UserEditForm(forms.Form):
    class Meta:
        model = Userfields =['first_name', 'last_name', 'email']

class ProfileEditForm(forms.Form):
    class Meta:
        model = Profile
        fields = ['date_of_birth', 'photo']
