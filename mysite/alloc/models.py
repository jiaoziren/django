from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models


@python_2_unicode_compatible
class Department(models.Model):
    """
    Department
    """
    dept_name = models.CharField(max_length=200)

    def __str__(self):
        return self.dept_name


class SLA(models.Model):
    """
    SLA
    """
    sla_text = models.CharField(max_length=200)

    def __str__(self):
        return self.sla_text


class Person(models.Model):
    """
    Person
    """
    person_name = models.CharField(max_length=200)

    def __str__(self):
        return self.person_name


class Application(models.Model):
    """
    Application
    """
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
