from django.contrib import admin
from .models import Department, Application, Person, SLA
# Register your models here.

admin.site.register(Department)
admin.site.register(Application)
admin.site.register(SLA)
admin.site.register(Person)