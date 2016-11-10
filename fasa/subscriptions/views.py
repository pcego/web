from django.shortcuts import render, resolve_url as r

from fasa.subscriptions.forms import SubscriptionForm
from django.template.loader import render_to_string
from django.core import mail
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.conf import settings
from fasa.subscriptions.models import Subscription



def new(request):


    if request.method == 'POST':
        return create(request)


    return empty_form(request)


def create(request):

    ## Atribue a variável form os dados vindos do formulário
    form = SubscriptionForm(request.POST)

    ## Verifica se o form possui erros
    if not form.is_valid():
        ## Form com erros então abortamos a execução do fluxo
        return render(request, 'subscriptions/subscription_form.html',
                      {'form': form})

    # Criando um objeto subscription carregado com os dados gravados no banco
    subscription = form.save()

    #subscription = Subscription.objects.create(**form.cleaned_data)

    ## chamada para a função auxiliar que envia email
    _send_mail('Confirmação de Incrição.',
               settings.DEFAULT_FROM_EMAIL,
               subscription.email,
               'subscriptions/subscription_email.txt',
               {'subscription': subscription})

    # Mudando o redirect para a rota da view detail
    # Passando como parâmetro a chave primária do objeto
    return HttpResponseRedirect(r('subscriptions:detail', subscription.uuid))


def empty_form(request):
    return render(request,'subscriptions/subscription_form.html', {'form':SubscriptionForm()})


def detail(request, uuid):
    subscription = Subscription.objects.get(uuid=uuid)
    return render(request, 'subscriptions/subscription_detail.html',
                  {'subscription': subscription})


def _send_mail(subject, from_, to, template_name, context):

    body = render_to_string(template_name, context)

    mail.send_mail(subject, body, from_, [from_, to])

