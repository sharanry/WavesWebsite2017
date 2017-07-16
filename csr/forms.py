from django import forms
from . import models





class register(forms.ModelForm):
  
  class Meta:
      model = models.CsrParticipant
      fields = [  'name',
                  'email',
                  'phone_number',
                  'city',
                  'address',
                  
              ]
      widgets = {
          'name': forms.TextInput(attrs = { 
                    'style': 'width: 35%; padding: 5px; margin: 5px;',
                    'placeholder': 'Name',
                                       }),
          'email':forms.EmailInput(attrs = { 
                    'style': 'width: 35%; padding: 5px; margin: 5px;',
                    'placeholder': 'Email',
                                       }),
          'phone_number':forms.TextInput(attrs = { 
                    'style': 'width: 35%; padding: 5px; margin: 5px;',
                    'placeholder': "Phone"
                                       }),
          'city': forms.TextInput(attrs = { 
                    'style': 'width: 35%; padding: 5px; margin: 5px;',
                    'placeholder': "City"
                                       }),
          'address':forms.Textarea(attrs = { 
                    'style': 'width: 71.5%;',
                    'rows': 5,
                    'placeholder': "Address"

                                       }),
      }