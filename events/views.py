from django.shortcuts import render
from django.views import View

# Create your views here.

class tshirt(View):
	def get (self, request, *args, **kwargs):
		context ={}

		return render(request, "events/tshirt.html", context)

	# def post(self, request, *args, **kwargs):

		
	# 	return render(request, template, context)
