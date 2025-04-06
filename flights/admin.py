from django.contrib import admin
from.models import Flight, City, Airline, SiteVisits


# Register your models here.
admin.site.register(Flight)
admin.site.register(City)
admin.site.register(Airline)
admin.site.register(SiteVisits)