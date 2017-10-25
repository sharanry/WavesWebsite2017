from django.shortcuts import render

# Create your views here.
from django.views import View


class home(View):
	def get (self, request, *args, **kwargs):
		context={}
		return render(request, "index2.html", context)

class beauvista(View):
	def get (self, request, *args, **kwargs):
		context={}
		return render(request, "beau_vista.html", context)

class carpedictum(View):
	def get (self, request, *args, **kwargs):
		context={}
		return render(request, "carpe_dictum.html", context)

class specials(View):
	def get (self, request, *args, **kwargs):
		context={}
		return render(request, "specials.html", context)		

class florence(View):
	def get (self, request, *args, **kwargs):
		context={}
		return render(request, "florence.html", context)

class events(View):
	def get (self, request, *args, **kwargs):
		context={}
		return render(request, "events2.html", context)
		underconstruction

class underconstruction(View):
	def get (self, request, *args, **kwargs):
		context={}
		return render(request, "under_construction.html", context)		

class contactus(View):
	def get (self, request, *args, **kwargs):
		context={}
		return render(request, "contact_us.html", context)		

class ourteam(View):
	def get (self, request, *args, **kwargs):
		context={}
		return render(request, "our_team.html", context)				

class sponsors(View):
	def get (self, request, *args, **kwargs):
		context={}
		return render(request, "sponsors.html", context)			