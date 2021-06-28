from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(
        label = 'Nome',
        widget = forms.TextInput(attrs={'placeholder': ''}))
    last_name = forms.CharField(
        label='Sobrenome',
        widget = forms.TextInput(attrs={'placeholder': ''}))
    email = forms.CharField(
        label='Email',
        widget = forms.TextInput(attrs={'placeholder': 'email@exemplo.com'}))
    password1 = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={'placeholder': ''}))
    password2 = forms.CharField(
        label='Confirmar senha',
        widget=forms.PasswordInput(attrs={'placeholder': ''}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']