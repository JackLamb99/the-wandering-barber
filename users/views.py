from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm


def register(request):
    """ Handles user registration by displaying a registration form and saving
    a new user if the form is valid. """
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Saves the new user
            messages.success(request, 'Your account has been created,'
                             'you can now log in.')
            # Redirect to login page after registration
            return redirect('login')
        else:  # If not a POST method, show an empty form
            form = UserRegistrationForm()
        return render(request, 'users/register.html', {'form': form})


def login_view(request):
    """ Handles user login by validating the provided credentials """
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Uses the overridden default Django 'username'
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # Authenticates using email as username
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {user.first_name}.')
                # Redirects to home upon successful login
                return redirect('index')
            else:  # If login details are invalid
                messages.error(request, 'Invalid email or password.')
        else:  # If login details are invalid
            messages.error(request, 'Invalid login details.')
    else:
        # Show empty login form for GET request
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    """ Logs the user out and redirects them to the homepage """
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    # Redirects to home upon successful logout
    return redirect('index')


@login_required
def my_account(request):
    return render(request, 'users/my_account.html')  # Render my_account.html
