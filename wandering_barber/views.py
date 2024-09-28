from django.shortcuts import render


# View for the home page
def index(request):
    return render(request, 'index.html')  # Render home.html


# View for the about page
def about(request):
    return render(request, 'about.html')  # Render about.html


# View for the contact page
def contact(request):
    return render(request, 'contact.html')  # Render contact.html
