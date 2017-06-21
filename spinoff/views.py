from django.shortcuts import render
from django.views import View

# Create your views here.
from .forms import register


from .models import SpinoffParticipant

class spinoffreg(View):
	def get (self, request, *args, **kwargs):
		form = register()
		
		context ={
			
			"form": form ,
			"event": "SpinOff",
			"url": "/spinoff/reg",
			"url_home": "/spinoff",
			"bkimg": "/static/spinoff.jpg",
			"bkimgh": "/static/hspinoff.jpg",
			"intro":"In one of the most popular events hosted by Waves, we ask you for one simple thing :",
			"intro2":"Spin to makes us groove and show us your DJ moves (apologise for the writer's poetic bend of mind) ",
			"intro3":'This event calls out to all those who often hear the line "DJ wale babu mera gana baja do" at birthday parties, sangeets and whatHaveYouNot.',
		}
		return render(request, "registration/event_reg_register.html", context)

	def post(self, request, *args, **kwargs):

		form = register(request.POST)
		
		template = "registration/event_reg_register.html"
		context={
				
				"form" : form,
				"event": "SpinOff",
				"url": "/spinoff/reg",
				"url_home": "/spinoff",
				"bkimg": "/static/spinoff.jpg",
				"bkimgh": "/static/hspinoff.jpg",
				"intro":"In one of the most popular events hosted by Waves, we ask you for one simple thing :",
				"intro2":"Spin to makes us groove and show us your DJ moves (apologise for the writer's poetic bend of mind) ",
				"intro3":'This event calls out to all those who often hear the line "DJ wale babu mera gana baja do" at birthday parties, sangeets and whatHaveYouNot.',
		
			}
		if form.is_valid():
			name = form. cleaned_data.get("name")
			place = form. cleaned_data.get("place")
			occupation = form. cleaned_data.get("occupation")
			preferredCity = form. cleaned_data.get("preferredCity")
			email = form.cleaned_data.get("email")
			phone_number = form.cleaned_data.get("phone_number")
			links_to_previous_performances = form. cleaned_data.get("links_to_previous_performances")



			# obj, created = SpinoffParticipant.objects.get_or_create(name=name, place=place, occupation=occupation, preferredCity=preferredCity, email= email, phone=phone, exp=exp)
			obj = SpinoffParticipant(name=name, place=place, occupation=occupation, preferredCity=preferredCity, email= email, phone_number=phone_number, links_to_previous_performances=links_to_previous_performances)
			
			try:
				obj.save()
			except:
				template = "registration/event_reg_failed.html"	
			
			template = "registration/event_reg_success.html"




		return render(request, template, context)
