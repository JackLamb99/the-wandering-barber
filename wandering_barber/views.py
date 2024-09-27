from django.shortcuts import render


# View for the home page
def home(request):
    return render(request, 'home.html')  # Render home.html


# View for the about page
def about(request):
    return render(request, 'about.html')  # Render about.html


# View for the booking page
def book(request):
    return render(request, 'book.html')  # Render book.html


# View for the contact page
def contact(request):
    return render(request, 'contact.html')  # Render contact.html
