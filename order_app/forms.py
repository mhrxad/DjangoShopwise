from django import forms
from django.contrib.auth.models import User
from django.core import validators


class UserNewOrderForm(forms.Form):
    product_id = forms.IntegerField(
        widget=forms.HiddenInput(),
    )

    count = forms.IntegerField(
        widget=forms.TextInput(attrs={
            'class': 'qty',
            'size': '4',
            'title': 'Qty'
        }
        ),
        initial=1
    )
