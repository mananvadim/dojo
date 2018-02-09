# -*- coding: utf-8 -*-


from django.conf.urls import include, url
from django.contrib import admin
from jsonrpc import jsonrpc_site
from jsonrpc import views as jsonrpc_views


urlpatterns = [

    url(r'^json/browse/', jsonrpc_views.browse, name='jsonrpc_browser'), # for the graphical browser/web console only, omissible
    url(r'^json/', jsonrpc_site.dispatch, name='jsonrpc_mountpoint'),
    #url(r'^json/(?P<method>[a-zA-Z0-9.]+)$', jsonrpc_site.dispatch), # for HTTP GET only, also omissible
    url(r'^app/', include('app.urls')),
    url(r'^admin/', admin.site.urls),

]