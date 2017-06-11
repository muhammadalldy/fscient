from django.conf.urls import url
#from mahasiswa import views
from . import views
from . import views as core_views
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [

    # url(r'^anggota/$', views.anggota, name='anggota'),
    url(r'anggota/', views.anggota, name='anggota'),
    url(r'^profil/', views.profil, name='profil'),
    url(r'^riset/', views.riset, name='riset'),
    url(r'^ebook/', views.ebook, name='ebook'),

    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^signup/$', core_views.signup, name='signup'),
    # # ex: /polls/5/0
    url(r'^profile/(?P<id>[0-9]+)/$', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # # ex: /polls/5/vote/
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),


    url(r'^model_form_upload/$', views.model_form_upload, name='model_form_upload'),
    url(r'^journal_form_upload/$', views.journal_form_upload, name='journal_form_upload'),
    url(r'^kontak/$', views.kontak, name='kontak'),
] 



