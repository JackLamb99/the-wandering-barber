from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),  # Registration page
    path('login/', views.login_view, name='login'),  # Login page
    path('logout/', views.logout_view, name='logout'),  # Logout functionality
    path('my_account/', views.my_account, name='my_account'),  # My Account Page
]
