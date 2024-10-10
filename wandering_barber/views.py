from django.shortcuts import render
from django.conf import settings


# View for the home page
def index(request):
    context = {
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
    }
    return render(request, 'index.html', context)  # Render index.html
