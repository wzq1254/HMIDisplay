# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class station_info(models.Model):
	#"""docstring for station_info"""
	station_name = models.CharField(max_length=30)
	station_state= models.CharField(max_length=30)
	def __str__(self):
		return self.station_state	
		#self.arg = arg
		