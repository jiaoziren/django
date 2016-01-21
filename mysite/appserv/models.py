from __future__ import unicode_literals

from django.db import models

class AppServ(models.Model):
	appserv_name = models.CharField(max_length=200)
	#appserv_desc = models.CharField(max_length=200)
	appserv_active = models.IntegerField(default=0)
	appserv_support_group = models.CharField(max_length=200)
	appserv_department = models.CharField(max_length=200)
	appserv_availability = models.CharField(max_length=200)
	appserv_team_member = models.CharField(max_length=200)
	appserv_business_owner = models.CharField(max_length=200)
	def __str__(self):
		return self.appserv_name