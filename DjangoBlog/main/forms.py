from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import *

class SearchForm(forms.Form):
    query = forms.CharField(label='Поиск', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))


class ContactUsForm(forms.ModelForm):
    name = forms.CharField(label='Ваше имя', max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Ваш Email', max_length=255, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label='Сообщение', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = ContactUsModel
        fields = ['name', 'email', 'message', ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-controlt'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'cols': 60, 'rows': 10}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Электронная почта', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Потверждение пароля',
                                widget=forms.PasswordInput(attrs={'class': 'password form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }



class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Логин'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))

    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Логин'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}),
        }

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = ['title', 'content', 'categories', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Контент'}),
            # 'categories': forms.SelectMultiple(attrs={'class': 'category-select'}),
            # 'tags': forms.CheckboxSelectMultiple(attrs={'class': 'tag-checkboxes', 'multiple': 'multiple'}),
        }
