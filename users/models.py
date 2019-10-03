from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date

class CustomUser(AbstractUser):

	# add additional fields in here
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	#date_of_birth = models.DateField(null=True, blank=True)
	#phone = models.CharField(max_length=20)
	#address = models.CharField(max_length=255)
	#state = models.CharField(max_length=30)
	#city = models.CharField(max_length=30)
	#zip_code = models.CharField(max_length=10)

	def __str__(self):
		return self.username