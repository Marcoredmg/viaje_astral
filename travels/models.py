from __future__ import unicode_literals

from django.db import models

class Travel(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	image = models.ImageField(blank=True)
	siteurl = models.CharField(max_length=255, blank=True)

	def __str__(self):
		return self.name
