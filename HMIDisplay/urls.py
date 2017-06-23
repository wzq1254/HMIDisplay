"""HMIDisplay URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import os
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles
from TemplateSet import CreateTemplate
from WebPostShow import views,ReceivePost

import settings
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #generate the template from general template
    url(r'^template-post/',CreateTemplate.Template_Post),
    #upper machine's labview post state & other information
    url(r'^labview-post/',ReceivePost.Labview_Post),
    #HMI visit the web
    url(r'^lists/(?P<table>\w+)/$',views.hello, name='station_name'),
    #HMI get the value from web
    url(r'^web-get',ReceivePost.Web_Get),
 ]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
