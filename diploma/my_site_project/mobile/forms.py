from django import forms
from .models import *

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):  # переопределили стандартную форму регистрации
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label="Подтверждение пароля", widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class RegisterForm(forms.Form):  # форма обратной связи (не связанная с моделью)
    name = forms.CharField(label="Имя", max_length=255)
    telephone = forms.CharField(label="Телефон", max_length=255)


class RegistrationForm(forms.Form):
    name = forms.CharField(label="Имя", max_length=255)
    telephone = forms.CharField(label="Телефон", max_length=255)

