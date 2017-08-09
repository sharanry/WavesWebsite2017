from django.db import models

# from django.core.validators import RegexValidator
# from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class DateTime(models.Model):
	creation_datetime = models.DateTimeField(auto_now_add=True)


class SpinoffParticipant(models.Model):
	CITIES = 	[	
					("Goa","Goa"),
					("Bangalore","Bangalore"),
		 			("Pune","Pune"),
		  			("Mumbai","Mumbai"),
		   			("Delhi","Delhi")
	   			]

	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100)
	place = models.CharField(max_length=100)
	occupation = models.CharField(max_length=100)
	preferredCity = models.CharField(choices=CITIES, max_length=20)
	email = models.EmailField()
	# phone_regex = RegexValidator( message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	# phone = models.IntegerField( min_value=1000000, max_value=99999999999, unique=True, )
	phone_number = models.CharField(max_length=12, unique=True)
	links_to_previous_performances = models.CharField( max_length=300, blank=True, null=True)

	creation_datetime = models.DateTimeField(auto_now_add=True)
	# datetime = models.ForeignKey(DateTime)
	# id = datetime
	# creation_datetime = datetime.get('creation_datetime')
	# objects = KirrURLManager()

	
	def save(self, *args, **kwargs):
		
		super(SpinoffParticipant, self).save(*args,**kwargs)	
	
	def __str__(self):
		return str(self.name)

	def __unicode__(self):
		return str(self.name)

# class SpinoffParticipantP(models.Model):

#     creation_datetime = models.DateTimeField(auto_now_add=True)
#     student = models.ForeignKey('SpinoffParticipant')