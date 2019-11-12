from django.contrib import admin

# Register your models here.
from .models import Country, City, Person, Reading

admin.site.register(Country)
admin.site.register(City)
admin.site.register(Person)
admin.site.register(Reading)
