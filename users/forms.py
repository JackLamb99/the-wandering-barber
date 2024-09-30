from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class UserRegistrationForm(UserCreationForm):
    """ Custom user registration form inheriting Django's built-in
    UserCreationForm """
    # Adds fields for first name, last name and email
    # All required for registration
    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    # Adds form-control class to password fields
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        """ Used to specify additional metadata about the form """
        model = User
        # Fields that will be shown in the form
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

    def clean_email(self):
        """ Checks if the email is already registered """
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email is already registered.")
        return email

    def save(self, commit=True):
        """ Overrides the default form save method """
        # Calls the save method of the parent form
        user = super(UserRegistrationForm, self).save(commit=False)
        # Sets the first name, last name and email
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        # Sets username to user's email
        user.username = self.cleaned_data['email']

        if commit:
            # Saves the user to the database
            user.save()

        return user
