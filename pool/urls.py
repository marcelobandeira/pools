from django.conf.urls import url
from pool import views

urlpatterns = [
   url(r'^$', views.index, name='index'),
   url(r'^question/(?P<question_id>\d+)$', views.question, name='question'),
   url(r'^question/(?P<question_id>\d+)/results$', views.results, name='results'),
   url(r'^question/(?P<question_id>\d+)/vote$', views.vote, name='vote'),
   url(r'^add_vote/(?P<choice_id>\d+)$', views.add_vote, name='add_vote'),
   url(r'^question/(?P<question_id>\d+)/manage$', views.manage, name='manage'),
   url(r'^question/(?P<question_id>\d+)/close$', views.close, name='close'),
   url(r'^question/(?P<question_id>\d+)/(?P<choice_id>\d+)/remove$', views.remove, name='remove'),
   url(r'^question/(?P<question_id>\d+)/(?P<choice_id>\d+)/add_to_question$', views.add_to_question, name='add_to_question'),


]