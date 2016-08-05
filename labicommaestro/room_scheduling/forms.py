# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from models import Reservation



class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Usuário", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Senha", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))

class RequireReservationForm(forms.Form):
    event_name = forms.CharField(max_length=400)
    start_datetime = forms.DateTimeField()
    end_datetime = forms.DateTimeField()
    room = forms.CharField(max_length=400)

    is_permanent = forms.BooleanField()


    weekday = forms.CharField(max_length=20)
