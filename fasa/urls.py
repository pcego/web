from django.conf.urls import url
from django.contrib import admin
from fasa.core.views import home
from fasa.subscriptions.views import subscribe, detail

urlpatterns = [
    url(r'^$', home),
    url(r'^inscricao/$', subscribe),
    url(r'^inscricao/([\w-]+)/$', detail),
    url(r'^admin/', admin.site.urls),
]
