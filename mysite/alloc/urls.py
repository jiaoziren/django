from django.conf.urls import url
from .views import AppView
from . import views


app_name = 'alloc'
urlpatterns = [
    url(r'^$', views.AppView.as_view(), name='apps'),
]
