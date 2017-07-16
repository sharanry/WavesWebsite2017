from django.shortcuts import render
from django.views import View
# Create your views here.

from .forms import register

from .models import CsrParticipant


class csr(View):
	
	def get (self, request, *args, **kwargs):
		context ={
		"event": "csr",
		"url": "/csr",
		"url_home": "/csr",
	}
		return render(request, "csr/intro.html", context)


class csrreg(View):
	def get (self, request, *args, **kwargs):
		form = register()
		
		context ={
			"form": form,
			"event": "csr",
			"url": "/csr/reg",
			"url_home": "/csr",
			
		}
		return render(request, "csr/reg.html", context)

	def post(self, request, *args, **kwargs):

		form = register(request.POST)
		
		template = "csr/intro.html"
		context ={
			
			"form": form ,
			"event": "csr",
			"url": "/csr/reg",
			"url_home": "/csr",
			
			}
		if form.is_valid():
			name = form. cleaned_data.get("name")
			email = form.cleaned_data.get("email")
			phone_number = form.cleaned_data.get("phone_number")
			city = form. cleaned_data.get("city")
			address = form. cleaned_data.get("address")

			
			
			obj = CsrParticipant(name=name, email= email, phone_number=phone_number, city=city, address=address)
			
			try:
				obj.save()
			except:
				template = "index.html"	
			
			# template = "csr/intro.html"

		return render(request, template, context)
