from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from . import forms


# Create your views here.

def login_view(request):
    if request.method != "POST":
        form = forms.LogInForm()
    else:
        form = forms.LogInForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('blogs:home')
            else:
                form.add_error(None, 'Invalid Username or Password')

    context = {'form': form}
    return render(request, 'users/login.html', context)


def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            authenticate_user = authenticate(request, username=new_user.username, password=request.POST['password1'])
            login(request, authenticate_user)
            return redirect('blogs:home')

    context = {'form': form}
    return render(request, 'users/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('blogs:index')
