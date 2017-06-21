from django.shortcuts import render
from django.views import View

# Create your views here.
from .forms import register


from .models import SmtfParticipant

class smtfreg(View):
	def get (self, request, *args, **kwargs):
		form = register()
		
		context ={
			
			"form": form ,
			"event": "Show Me The Funny",
			"url": "/smtf/reg",
			"url_home": "/smtf",
			"bkimg": "/static/smtf.jpg",
			"bkimgh": "/static/hsmtf.jpg"
			
		}
		return render(request, "registration/event_reg_register.html", context)

	def post(self, request, *args, **kwargs):

		form = register(request.POST)
		
		template = "registration/event_reg_register.html"
		context ={
			
			"form": form ,
			"event": "Show Me The Funny",
			"url": "/smtf/reg",
			"url_home": "/smtf",
			"bkimg": "/static/smtf.jpg",
			"bkimgh": "/static/hsmtf.jpg"

			
		}
		if form.is_valid():
			name = form. cleaned_data.get("name")
			place = form. cleaned_data.get("place")
			occupation = form. cleaned_data.get("occupation")
			preferredCity = form. cleaned_data.get("preferredCity")
			email = form.cleaned_data.get("email")
			phone_number = form.cleaned_data.get("phone_number")
			links_to_previous_performances = form. cleaned_data.get("links_to_previous_performances")



			
			obj = SmtfParticipant(name=name, place=place, occupation=occupation, preferredCity=preferredCity, email= email, phone_number=phone_number, links_to_previous_performances=links_to_previous_performances)
			
			try:
				obj.save()
			except:
				template = "registration/event_reg_failed.html"	
			
			template = "registration/event_reg_success.html"




		return render(request, template, context)
