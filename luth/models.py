from django.db import models

class About(models.Model):
	bio = models.TextField()

class Contact(models.Model):
	name = models.CharField(max_length=30, blank=False)
	message = models.CharField(max_length=128, blank=False)
	email = models.EmailField(max_length=70, blank=False)