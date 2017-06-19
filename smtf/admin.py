from django.contrib import admin

# Register your models here.

from .models import SmtfParticipant
class AdminSettings(admin.ModelAdmin):
    # define which columns displayed in changelist
    list_display = (
    				'id',
    				'name',
                  'place',
                  'occupation',
                  'preferredCity',
                  'email',
                  'phone_number',
                  'prior_experience_if_any',
                  'creation_datetime')
    # add filtering by date
    list_filter = ('creation_datetime',)
    # add search field 
    search_fields = ['name', 'email', 'phone_number', 'place']

admin.site.register(SmtfParticipant, AdminSettings)
