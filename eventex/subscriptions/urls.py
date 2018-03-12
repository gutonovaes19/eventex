
from django.conf.urls import url

from eventex.subscriptions.views import new, detail

#url(r'^inscricao/(\d+)/$', detail) --- group match
urlpatterns = [
    url(r'^$', new, name = 'new'),
    url(r'^(\d+)/$', detail, name='detail'),
]
