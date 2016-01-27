# from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponseRedirect
# from django.core.urlresolvers import reverse
from django.views import generic
from .models import Application


class AppView(generic.ListView):
    template_name = 'alloc/app.html'
    context_object_name = 'app_list'

    def get_queryset(self):
        return Application.objects.all()


class SlaView(generic.ListView):
    """
    TODO
    """
    template_name = ''
    context_object_name = 'sla_list'

    def get_queryset(self):
        # return Application.objects.filter(app_dept=)
        pass


class DeptView(generic.ListView):
    """
    TODO
    """
    pass


class PrimaryContactView(generic.ListView):
    """
    TODO
    """
    pass


class SecondaryContactView(generic.ListView):
    """
    TODO
    """
    pass
