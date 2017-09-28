from django.shortcuts import render
from django.views import View
# Create your views here.

from .forms import register

from .models import Participant
class reg(View):
	def get (self, request, *args, **kwargs):
		form = register()
		
		context ={
			"form": form,
			"event": "Waves Registration",
			"url": "/reg",
			"url_home": "/",
			
		}
		return render(request, "registration/reg.html", context)

	def post(self, request, *args, **kwargs):

		form = register(request.POST)
		
		template = "registration/reg.html"
		context ={
			"form": form,
			"event": "Waves Registration",
			"url": "/reg/",
			"url_home": "/",
			
		}
		if form.is_valid():
			email = form.cleaned_data.get("email")
			name = form. cleaned_data.get("name")
			college = form.cleaned_data.get("college")
			event = form.cleaned_data.get("event")
			phone_number = form.cleaned_data.get("phone_number")
			# city = form. cleaned_data.get("city")
			# address = form. cleaned_data.get("address")

			
			
			obj = Participant(name=name, email= email, phone_number=phone_number, college=college, event=event)
			
			try:
				obj.save()
				template = "registration/success.html"
			except:
				template = "registration/failure.html"	
			
			# template = "registration/wavesRegSuccess.html"

		return render(request, template, context)
