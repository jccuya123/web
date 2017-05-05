# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class ServerModel(models.Model):
	name = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	emailid = models.CharField(max_length=20)
	#password = models.CharField(max_length=50)

	def __unicode__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('servers_update', kwargs={'pk':self.pk})