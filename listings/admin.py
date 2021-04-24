#
# Admin page configuration for Listings
#

from django.contrib import admin
from .models import *

# Register the Listing model on the Admin page
admin.site.register(Listings)
# Register the Update model on the Admin page
admin.site.register(Update)
