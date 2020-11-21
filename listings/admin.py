from django.contrib import admin
from .models import AddListings, CurrentListings, ModifyListings
# Register your models here.

admin.site.register(AddListings)
admin.site.register(ModifyListings)
admin.site.register(CurrentListings)