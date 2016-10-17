from django.contrib import admin
from fasa.subscriptions.models import Subscription
from django.utils.timezone import now


class SubscriptionModelAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'phone', 'cpf', 'created_at', 'subscribed_today')
    date_hierarchy = 'created_at'
    search_fields = ('name', 'email', 'phone', 'cpf', 'created_at')
    list_filter = ('created_at',)

    # Para maiores detalhes sobre este método
    # leia a documentação do admin do django
    # https://docs.djangoproject.com/en/1.10/ref/contrib/admin/
    def subscribed_today(self, obj):
        #retorna True ou False
        return obj.created_at.date() == now().date()

    subscribed_today.short_description = 'Inscrito Hoje?'

    # Código adicionado para criar o marcador gráfico
    subscribed_today.boolean = True


admin.site.register(Subscription, SubscriptionModelAdmin)
