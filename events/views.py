from django.shortcuts import render
from django.views import View

# Create your views here.

class tshirt(View):
	def get (self, request, *args, **kwargs):
		context ={}

		return render(request, "events/tshirt.html", context)


class moot(View):
	def get (self, request, *args, **kwargs):
		context ={}

		return render(request, "events/moot.html", context)

class caricreatures(View):
	def get (self, request, *args, **kwargs):
		context ={}

		return render(request, "events/caricreatures.html", context)


class doodle(View):
	def get (self, request, *args, **kwargs):
		context ={}

		return render(request, "events/doodle.html", context)

class ohSnap(View):
	def get (self, request, *args, **kwargs):
		context ={}

		return render(request, "events/oh_snap.html", context)

class short(View):
	def get (self, request, *args, **kwargs):
		context ={}

		return render(request, "events/short.html", context)	