from django.shortcuts import render
from .models import AppServ

# Create your views here.
def index(request):
    appserv_list = AppServ.objects.order_by('appserv_name')[:500]
    context = {'appserv_list': appserv_list}
    return render(request, 'appserv/index.html', context)

def detail(request, appserv_id):
	return HttpResponse("You are looking at %s." % appserv_id)
