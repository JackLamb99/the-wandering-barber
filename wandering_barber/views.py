from django.shortcuts import render
from django.conf import settings


# View for the home page
def index(request):
    context = {
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
    }
    return render(request, 'index.html', context)  # Render home.html


# View for the about page
def about(request):
    return render(request, 'about.html')  # Render about.html


# View for the contact page
def contact(request):
    return render(request, 'contact.html')  # Render contact.html
