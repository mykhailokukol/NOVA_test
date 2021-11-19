from django import forms
from . import models


class ContactForm(forms.Form):
    """Универсальная форма заполнения данных Контакта"""

    name = forms.CharField(
        max_length=255,
        required=True,
        label='Имя'
    )
    email = forms.CharField(
        widget=forms.EmailInput,
        required=False,
        label='Электронная почта'
    )
    phone = forms.CharField(
        max_length=15, 
        required=False,
        label='Номер телефона'
    )
