from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models

@python_2_unicode_compatible

# Department
class Department(models.Model):
	dept_name = models.CharField(max_length=200)
	def __str__(self):
		return self.dept_name

# SLA
class SLA(models.Model):
	sla_text = models.CharField(max_length=200)
	def __str__(self):
		return self.sla_text

# Person
class Person(models.Model):
	person_name = models.CharField(max_length=200)
	def __str__(self):
		return self.person_name

# App
class Application(models.Model):
	app_name = models.CharField(max_length=200)
	app_dept = models.CharField(max_length=200)
	app_sla = models.CharField(max_length=200)
	app_primary = models.CharField(max_length=200)
	app_secondary = models.CharField(max_length=200)
	app_dept = models.ForeignKey(Department)
	app_sla = models.ForeignKey(SLA)
	app_primary = models.ForeignKey(Person, related_name='primary')
	app_secondary = models.ForeignKey(Person, related_name='secondary')

	def __str__(self):
		return self.app_name