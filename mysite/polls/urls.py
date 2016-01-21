from django.conf.urls import url
from .views import QuestionCreate, QuestionUpdate, QuestionDelete
from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(),
        name='results'),
    # why do I have to use question_id instead of pk below?
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'question/add/$', QuestionCreate.as_view(), name='question-add'),
    url(r'question/(?P<pk>[0-9]+)/$', QuestionUpdate.as_view(),
        name='question-update'),
    url(r'question/(?P<pk>[0-9]+)/delete/$', QuestionDelete.as_view(),
        name='question-delete'),
]
