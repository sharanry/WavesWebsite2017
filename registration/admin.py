from django.contrib import admin

# Register your models here.
from .models import Participant


class AdminSettings(admin.ModelAdmin):
    # define which columns displayed in changelist
    list_display = (
    				'id',
    				'email',
	                'name',
	                'phone_number',
	                'college',
	                'event',
	                'creation_datetime')
    # add filtering by date
    list_filter = ('creation_datetime',)
    # add search field 
    search_fields = ['college','name', 'email', 'phone_number', 'city']

admin.site.register(Participant, AdminSettings)
