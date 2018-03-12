
from django.conf.urls import include, url
from django.contrib import admin
from eventex.core.views import home


#url(r'^inscricao/(\d+)/$', detail) --- group match
#url(r'', --> expressao regular vazia faz math com qq string
urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'înscricao/',include('eventex.subscriptions.urls',
                              namespace='subscriptions')),
    url(r'^admin/', include(admin.site.urls)),
]
