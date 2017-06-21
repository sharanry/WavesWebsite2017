from django import forms
from . import models





class register(forms.ModelForm):
  links_to_previous_performances = forms.CharField(required=False, max_length=300,  widget=forms.Textarea)
  class Meta:
      model = models.SpinoffParticipant
      fields = [  'name',
                  'place',
                  'occupation',
                  'preferredCity',
                  'email',
                  'phone_number',
                  'links_to_previous_performances'
              ]