"""workhuntr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
  https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
  1. Add an import:  from my_app import views
  2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
  1. Add an import:  from other_app.views import Home
  2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
  1. Import the include() function: from django.urls import include, path
  2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from listings import views as listing_views
from workhuntr import views as workhuntr_views

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', workhuntr_views.home, name='home'),
  path('create_account/', user_views.create_account, name='create_account'),
  path('profile/', user_views.profile, name='profile'),
  path('edit_profile/', user_views.edit_profile, name='edit_profile'),
  path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
  path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
  path('dashboard/', workhuntr_views.dashboard, name='dashboard'),
  path('create_listings', listing_views.create_listings, name='create_listings'),
  path('current_listings',listing_views.current_listings, name='current_listings'),
  path('modify_listings/<str:pk>/', listing_views.modify_listings, name='modify_listings'),
  path('delete_listing/<str:pk>/', listing_views.delete_listing, name='delete_listing')
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
