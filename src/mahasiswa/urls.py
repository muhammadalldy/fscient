from django.conf.urls import url
#from mahasiswa import views
from . import views
from . import views as core_views
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [
    # url(r'^$', views.mahasiswa_list),
    # url(r'^mahasiswa/(?P<pk>[0-9]+)/$', views.mahasiswa_detail),

    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^signup/$', core_views.signup, name='signup'),
    # # ex: /polls/5/0
    url(r'^mahasiswa/(?P<id>[0-9]+)/$', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # # ex: /polls/5/vote/
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

]



