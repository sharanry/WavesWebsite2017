from django.db import models

# Create your models here.
class DateTime(models.Model):
	creation_datetime = models.DateTimeField(auto_now_add=True)


class InverseParticipant(models.Model):
	# Blore pune mumbai
	CITIES = 	[	
					("Goa","Goa"),
					("Bangalore","Bangalore"),
		 			("Pune","Pune"),
		  			("Mumbai","Mumbai"),
		   			
	   			]

	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	place = models.CharField(max_length=100)
	occupation = models.CharField(max_length=100)
	preferredCity = models.CharField(choices=CITIES, max_length=20)
	email = models.EmailField()
	phone_number = models.CharField(max_length=12, unique=True)
	links_to_previous_performances = models.CharField( max_length=300, blank=True, null=True)

	creation_datetime = models.DateTimeField(auto_now_add=True)
	
	
	def save(self, *args, **kwargs):
		
		super(InverseParticipant, self).save(*args,**kwargs)	
	
	def __str__(self):
		return str(self.name)

	def __unicode__(self):
		return str(self.name)

