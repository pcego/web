from django.shortcuts import render

from fasa.subscriptions.forms import SubscriptionForm
from django.template.loader import render_to_string
from django.core import mail
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.conf import settings
from fasa.subscriptions.models import Subscription


def subscribe(request):


    if request.method == 'POST':
        return create(request)

    else:
        return new(request)


def create(request):

    ## Atribue a variável form os dados vindos do formulário
    form = SubscriptionForm(request.POST)

    ## Verifica se o form possui erros
    if not form.is_valid():
        ## Form com erros então abortamos a execução do fluxo
        return render(request, 'subscriptions/subscription_form.html',
                      {'form': form})

    ## chamada para a função auxiliar que envia email
    _send_mail('Confirmação de Incrição.',
               settings.DEFAULT_FROM_EMAIL,
               form.cleaned_data['email'],
               'subscriptions/subscription_email.txt',
               form.cleaned_data)

    Subscription.objects.create(**form.cleaned_data)

    messages.success(request, 'Inscrição Realizada com Sucesso!')

    return HttpResponseRedirect('/inscricao/')



def new(request):
    return render(request,'subscriptions/subscription_form.html', {'form':SubscriptionForm()})


def _send_mail(subject, from_, to, template_name, context):

    body = render_to_string(template_name, context)

    mail.send_mail(subject, body, from_, [from_, to])

