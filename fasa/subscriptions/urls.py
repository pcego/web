from django.conf.urls import url
from fasa.subscriptions.views import subscribe, detail

urlpatterns = [

    url(r'^inscricao/$', subscribe, name='new'),
    url(r'^inscricao/([\w-]+)/$', detail, name='detail'),

]
