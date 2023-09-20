from django.contrib import admin
from .models import TeachingRegistration,ScoutingRegistration,VolenteerRegistration,Choice

admin.site.register(TeachingRegistration)
admin.site.register(Choice)
admin.site.register(ScoutingRegistration)
admin.site.register(VolenteerRegistration)
# Register your models here.
