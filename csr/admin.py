from django.contrib import admin

# Register your models here.
from .models import CsrParticipant


class AdminSettings(admin.ModelAdmin):
    # define which columns displayed in changelist
    list_display = (
    				'id',
    				'name',
	                'email',
	                'phone_number',
	                'city',
	                'address',
	                'creation_datetime')
    # add filtering by date
    list_filter = ('creation_datetime',)
    # add search field 
    search_fields = ['name', 'email', 'phone_number', 'city']

admin.site.register(CsrParticipant, AdminSettings)
