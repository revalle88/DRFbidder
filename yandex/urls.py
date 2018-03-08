from django.urls import path, re_path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^keywords/(?P<campaign_id>\d+)/', views.keywords, name='keywords'),
    #path('keywords/(?P<campaign_id>\w{0,50})/$', views.keywords, name='keywords'),
]
