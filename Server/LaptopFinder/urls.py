"""LaptopFinder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url

from apps.database_manager.api import *
from apps.text_analyzer.api import *

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/users_list/$', UserList.as_view(), name='user_list'),
    url(r'^api/users_list/(?P<user_id>\d+)/$',
        UserDetail.as_view(), name='user_list'),
    url(r'^api/laptops_by_brand/(?P<laptop_brand>\w+)/$', Laptop_By_Brand.as_view(), name='laptop_list'),
    url(r'^api/laptops_by_analyzer/(?P<text>\w+)/$', Text_Analyzer.as_view(), name='laptops'),
    url(r'^api/laptops_by_price/(?P<laptop_price>\w+)/$', Laptops_By_Price.as_view(), name='laptops_by_price'),
    url(r'^api/auth/$', UserAuthentication.as_view(),
        name='User Authentication Api'),
]

