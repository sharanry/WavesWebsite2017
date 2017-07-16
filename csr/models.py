from django.db import models

# Create your models here.
class DateTime(models.Model):
	creation_datetime = models.DateTimeField(auto_now_add=True)


class CsrParticipant(models.Model):
	# Blore pune mumbai
	# CITIES = 	[	
	# 				("Bangalore","Bangalore"),
	# 	 			("Pune","Pune"),
	# 	  			("Mumbai","Mumbai"),
		   			
	#    			]

	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	email = models.EmailField()
	phone_number = models.CharField(max_length=12, unique=True)
	city = models.CharField(max_length=100)
	address = models.CharField(max_length=300)
	creation_datetime = models.DateTimeField(auto_now_add=True)
	
	
	def save(self, *args, **kwargs):
		
		super(CsrParticipant, self).save(*args,**kwargs)	
	
	def __str__(self):
		return str(self.name)

	def __unicode__(self):
		return str(self.name)
