from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(),
        name='results'),
    # generic view uses pk but the following view is not generic
    # hence using <question_id>
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]