from django import forms


class LogInForm(forms.Form):
    username = forms.CharField(empty_value='username', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
