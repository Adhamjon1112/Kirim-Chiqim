from django import forms
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from .models import Transaction

User = get_user_model()


class UserRegistrationForm(ModelForm):
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
        'class': 'p-2 border border-slate-500 rounded w-full',
    }), label="Parol")
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
        'class': 'p-2 border border-slate-500 rounded w-full',
    }), label="Parolni tasdiqlang")

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                   'password1', 'password2']

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'p-2 border border-slate-500 rounded w-full'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'p-2 border border-slate-500 rounded w-full'
            }),
            'username': forms.TextInput(attrs={
                'class': 'p-2 border border-slate-500 rounded w-full'
            }),
        }


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['type', 'amount', 'description']
        exclude = ['date']
