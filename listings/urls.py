from django.urls import path
from . import views

app_name = 'listings'

urlpatterns = [
    path('/create_listings', views.create_listings, name='create_listings'),
    path('/current_listings', views.current_listings, name = 'current_listings'),
    path('/modify_listings/<str:pk>/', views.modify_listings, name = 'modify_listings'),
    path('/delete_listing/<str:pk>/', views.delete_listing, name = 'delete_listing')
]