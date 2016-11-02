from django.contrib import admin
from fasa.subscriptions.models import Subscription
from django.utils.timezone import now


class SubscriptionModelAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'phone', 'cpf', 'created_at', 'subscribed_today', 'paid')
    date_hierarchy = 'created_at'
    search_fields = ('name', 'email', 'phone', 'cpf', 'created_at')
    list_filter = ('paid', 'created_at',)

    actions = ['mark_as_paid']

    # Para maiores detalhes sobre este método
    # leia a documentação do admin do django
    # https://docs.djangoproject.com/en/1.10/ref/contrib/admin/
    def subscribed_today(self, obj):
        #retorna True ou False
        return obj.created_at.date() == now().date()

    subscribed_today.short_description = 'Inscrito Hoje?'

    # Código adicionado para criar o marcador gráfico
    subscribed_today.boolean = True

    # Este método recebe como parâmetro uma instância de modelAdmin
    # o request e um queryset
    def mark_as_paid(self, request, queryset):
        # recebe a quant de linhas q sofreram update
        count = queryset.update(paid=True)

        if count == 1:
            msg = '{} Inscrição marcada como paga'
        else:
            msg = '{} Inscrições marcadas como pagas'

        self.message_user(request, msg.format(count))


    mark_as_paid.short_description = 'Marcar Selecionados como Pago'


admin.site.register(Subscription, SubscriptionModelAdmin)
