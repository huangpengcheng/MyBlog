#coding=utf-8
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='',max_length=15)
    password = forms.CharField(label='',max_length=300)
