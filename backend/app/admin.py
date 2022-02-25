from django.contrib import admin

# Register your models here.
from .models import Source, Organization

admin.site.register(Source)
admin.site.register(Organization)