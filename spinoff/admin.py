from django.contrib import admin

# Register your models here.


from .models import SpinoffParticipant


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
                  # 'prior_experience_if_any',
                  'links_to_previous_performances',
                  'creation_datetime')
    # add filtering by date
    list_filter = ('creation_datetime',)
    # add search field 
    search_fields = ['name', 'email', 'phone_number', 'place']

admin.site.register(SpinoffParticipant, AdminSettings)
