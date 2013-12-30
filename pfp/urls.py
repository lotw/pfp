from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.static import * 
from pfp.views import *
from pinMachines.views import *
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^blog/', include('blog.urls')),
    #url(r'^admin/', include(admin.site.urls)),

    url(r'^$', homepage, name='home'),
    url(r'^machines/', machinesPage, name='machinesPage'),
    url(r'^tournaments/', tournamentsPage, name='tournamentsPage'),

    # the urls for the various AJAX calls
    url(r'^ajax/addMachine/', ajaxAddMachine, name='ajaxAddMachine'),
    url(r'^ajax/addLocation/', ajaxAddLocation, name='ajaxAddLocation'),
    url(r'^ajax/assignMachine/', ajaxAssignMachine, name='ajaxAssignMachine'),
)
