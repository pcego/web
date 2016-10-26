from django.conf.urls import url, include
from django.contrib import admin
from fasa.core.views import home


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'', include('fasa.subscriptions.urls', namespace='subscriptions')),
    url(r'^admin/', admin.site.urls),
]
