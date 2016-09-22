from django.conf.urls import url
from django.contrib import admin
from fasa.core.views import home
from fasa.subscriptions.views import subscribe

urlpatterns = [
    url(r'^$', home),
    url(r'^inscricao/$', subscribe),
    url(r'^admin/', admin.site.urls),
]
