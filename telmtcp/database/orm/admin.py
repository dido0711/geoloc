from django.contrib import admin
from telmtcp.database.orm.models import *

class GeolocationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in geolocation._meta.get_fields()]

admin.site.register(geolocation, GeolocationAdmin)
