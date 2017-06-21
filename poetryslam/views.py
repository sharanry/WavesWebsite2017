from django.shortcuts import render
from django.views import View

# Create your views here.
from .forms import register


from .models import InverseParticipant

class inversereg(View):
	def get (self, request, *args, **kwargs):
		form = register()
		
		context ={
			
			"form": form ,
			"event": "inVerse",
			"url": "/inverse/reg",
			"url_home": "/inverse",
			"bkimg": "/static/poetryslam.jpeg",
			"bkimgh": "/static/hpoetryslam.jpeg",
			"intro":"This event is all about presenting the spoken word. Blank verses or meters, first love or breakup poem, humorous poems or melancholic ones, we are on the lookout for all styles of poetry.",
			"intro2":"This national event, with qualifiers in Bangalore, Mumbai, Pune, and Goa and the finals in BITS Goa, aims to find the best poets at the national collegiate level. With a chance to perform in front of a mouth-watering line-up of established poets who will preside as the judges, a chance to feature on Poetry Slam Inc's YouTube channel, and cash and kind incentives all along the way, this is one Poetry Slam competition you cannot afford to miss.",	
			"intro3":"",
		}
		return render(request, "registration/event_reg_register.html", context)

	def post(self, request, *args, **kwargs):

		form = register(request.POST)
		
		template = "registration/event_reg_register.html"
		context ={
			
			"form": form ,
			"event": "inVerse",
			"url": "/inverse/reg",
			"url_home": "/inverse",
			"bkimg": "/static/poetryslam.jpeg",
			"bkimgh": "/static/hpoetryslam.jpeg",
			"intro":"This event is all about presenting the spoken word. Blank verses or meters, first love or breakup poem, humorous poems or melancholic ones, we are on the lookout for all styles of poetry.",
			"intro2":"This national event, with qualifiers in Bangalore, Mumbai, Pune, and Goa and the finals in BITS Goa, aims to find the best poets at the national collegiate level. With a chance to perform in front of a mouth-watering line-up of established poets who will preside as the judges, a chance to feature on Poetry Slam Inc's YouTube channel, and cash and kind incentives all along the way, this is one Poetry Slam competition you cannot afford to miss.",	
			"intro3":"",
			}
		if form.is_valid():
			name = form. cleaned_data.get("name")
			place = form. cleaned_data.get("place")
			occupation = form. cleaned_data.get("occupation")
			preferredCity = form. cleaned_data.get("preferredCity")
			email = form.cleaned_data.get("email")
			phone_number = form.cleaned_data.get("phone_number")
			links_to_previous_performances = form. cleaned_data.get("links_to_previous_performances")



			
			obj = InverseParticipant(name=name, place=place, occupation=occupation, preferredCity=preferredCity, email= email, phone_number=phone_number, links_to_previous_performances=links_to_previous_performances)
			
			try:
				obj.save()
			except:
				template = "registration/event_reg_failed.html"	
			
			template = "registration/event_reg_success.html"




		return render(request, template, context)
