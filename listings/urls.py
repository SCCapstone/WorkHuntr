from django.urls import path

from . import views

app_name = 'listings'

urlpatterns = [
    path('', views.current_listings, name='current_listings'),
]