"""Branch_change URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url,patterns
from django.contrib import admin
from login.views import *
from input.views import *
from django.conf.urls.static import static
from django.conf import settings 
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',empty_view),
    url(r'^home/$', home_view),
    url(r'^logout/$', logout_view),
 #   url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    url(r'^register/$', register_view),
    url(r'^register/success/$', register_success_view),
	url(r'^fillform/$',fillform_view),    
    url(r'^thanks/$',thanks_view), 
    url(r'^admin1/$',admin_view), 
    url(r'^update/$',update_view), 
    url(r'^delete/$',delete),  
    url(r'^admin1/table/$',data_view),
    url(r'^admin1/algorithm/$',onwhat),  
    url(r'^admin1/roll_to_cpi/$',roll_to_cpi),
    url(r'^download/(?P<file_name>.+)$', download), 
    url(r'^admin1/algorithm/code1/$',code_1),
    url(r'^admin1/algorithm/code2/$',code_2),
        
]
urlpatterns += [
    url(r'^admin1/',include('login.urls')),
    #url(r'uploa^$', RedirectView.as_view(url='/upload/list/', permanent=True)),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
     