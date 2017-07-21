from django.db import models

# Create your models here.
class DateTime(models.Model):
	creation_datetime = models.DateTimeField(auto_now_add=True)


class Participant(models.Model):
	

	id = models.AutoField(primary_key=True)
	email = models.EmailField()
	name = models.CharField(max_length=100)
	college = models.CharField(max_length=100)
	event = models.CharField(max_length=100)
	phone_number = models.CharField(max_length=12, unique=True)
	# city = models.CharField(max_length=100)
	# address = models.CharField(max_length=300)
	creation_datetime = models.DateTimeField(auto_now_add=True)
	
	
	def save(self, *args, **kwargs):
		
		super(Participant, self).save(*args,**kwargs)	
	
	def __str__(self):
		return str(self.name)

	def __unicode__(self):
		return str(self.name)
