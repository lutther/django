from django.db import models

class Province(models.Model):
	name = models.CharField(max_length=30, blank=False)

	def __unicode__(self):
		return self.name

class Business(models.Model):
	province = models.ForeignKey(Province)
	name = models.CharField(max_length=128, blank=False)
	address = models.CharField(max_length=70, blank=False)
	contact = models.IntegerField(blank=False)
	b_type = models.CharField(max_length=30, blank=False)
	suburb = models.CharField(max_length=30, blank=False)

	def __unicode__(self):
		return self.name
