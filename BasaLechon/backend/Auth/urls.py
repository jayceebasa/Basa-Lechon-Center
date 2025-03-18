from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('auth/google/', include('allauth.socialaccount.urls')),
]