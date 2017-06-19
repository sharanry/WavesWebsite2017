from django import forms
from . import models





class register(forms.ModelForm):
  prior_experience_if_any = forms.CharField(required=False, max_length=300,  widget=forms.Textarea)
  class Meta:
      model = models.SmtfParticipant
      fields = [  'name',
                  'place',
                  'occupation',
                  'preferredCity',
                  'email',
                  'phone_number',
                  'prior_experience_if_any'
              ]