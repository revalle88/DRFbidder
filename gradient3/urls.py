"""gradient3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView
from rest_framework import routers
from django.conf.urls import url, include
from bidder import views
from bidder.views import CampaignKeywordList, KeywordList, KeywordDetail

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'campaigns', views.CampaignViewSet)
#router.register(r'keywords', views.KeywordViewSet)

urlpatterns = [
  path('admin/', admin.site.urls),
  path('yandex/', include('yandex.urls')),

  url(r'^/(?P<keyword>[0-9a-zA-Z_-]+)$', KeywordDetail.as_view(), name='keyword-detail'),
  #url(r'^api/keywords$', KeywordList.as_view(), name = 'keyword-list'),


  re_path('api/(?P<directId>[0-9a-zA-Z_-]+)/keywords', CampaignKeywordList.as_view(), name = 'keyword-list'),
  path('api/', include('bidder.urls')),
  path('api/', include(router.urls)),
  #re_path('.*', TemplateView.as_view(template_name='index.html')),
  #url(r'^', include(router.urls)),
 
]