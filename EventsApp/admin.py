from django.contrib import admin

from EventsApp.models import AddEvents
from django.contrib import admin
# Register your models here.

class AdminAddEvents(admin.ModelAdmin):
    list_display = ['EventName','EventImg','EventDesc','EventType','EventCost','EventDuration','EventStartDate']

admin.site.register(AddEvents,AdminAddEvents)