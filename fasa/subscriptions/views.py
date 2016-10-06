from django.shortcuts import render

from fasa.subscriptions.forms import SubscriptionForm
from django.template.loader import render_to_string
from django.core import mail
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.conf import settings
from fasa.subscriptions.models import Subscription


def subscribe(request):


    ## Verifica se o método da requisição é POST
    if request.method == 'POST':
        ## Atribue a variável form os dados vindos do formulário
        form = SubscriptionForm(request.POST)

        ## Método que trata os dados recebidos do formulário
        ## e os converte para objetos python de alto nível
        ## aplicando o metodo full_clean() no processo
        if form.is_valid():

            ## O cleaned_data é um dicionário
            ## com o dados já tratados pelo full_clean()
            data = form.cleaned_data
            body = render_to_string('subscriptions/subscription_email.txt',
                                    data)

            mail.send_mail('Confirmação de Incrição.',
                           body,
                           'contato@fasa.edu.br',
                           ['contato@fasa.edu.br', data['email']])

            Subscription.objects.create(**form.cleaned_data)

            messages.success(request, 'Inscrição Realizada com Sucesso!')

            return HttpResponseRedirect('/inscricao/')

        else:
            return render(request, 'subscriptions/subscription_form.html',
                          {'form': form})


    else:
        context = {'form':SubscriptionForm()}
        return render(request,'subscriptions/subscription_form.html', context)

# PRIMEIRA REFATORAÇÃO

#     if request.method == 'POST':
#         return create(request)
#
#     else:
#         return new(request)
#
#
# def create(request):
#
#     ## Atribue a variável form os dados vindos do formulário
#     form = SubscriptionForm(request.POST)
#
#     ## Método que trata os dados recebidos do formulário
#     ## e os converte para objetos python de alto nível
#     ## aplicando o metodo full_clean() no processo
#     if form.is_valid():
#
#         ## O cleaned_data é um dicionário
#         ## com o dados já tratados pelo full_clean()
#         data = form.cleaned_data
#         body = render_to_string('subscriptions/subscription_email.txt',
#                                 data)
#
#         mail.send_mail('Confirmação de Incrição.',
#                         body,
#                         'contato@fasa.edu.br',
#                         ['contato@fasa.edu.br', data['email']])
#
#         messages.success(request, 'Inscrição Realizada com Sucesso!')
#
#         return HttpResponseRedirect('/inscricao/')
#
#     else:
#         return render(request, 'subscriptions/subscription_form.html',
#                       {'form': form})
#
#
# def new(request):
#
#     context = {'form':SubscriptionForm()}
#     return render(request,'subscriptions/subscription_form.html', context)

# REFATORAÇÃO FINAL

#     if request.method == 'POST':
#         return create(request)
#
#     else:
#         return new(request)
#
#
# def create(request):
#
#     ## Atribue a variável form os dados vindos do formulário
#     form = SubscriptionForm(request.POST)
#
#     ## Verifica se o form possui erros
#     if not form.is_valid():
#         ## Form com erros então abortamos a execução do fluxo
#         return render(request, 'subscriptions/subscription_form.html',
#                       {'form': form})
#
#     ## chamada para a função auxiliar que envia email
#     _send_mail('Confirmação de Incrição.',
#                settings.DEFAULT_FROM_EMAIL,
#                form.cleaned_data['email'],
#                'subscriptions/subscription_email.txt',
#                form.cleaned_data)
#
#     messages.success(request, 'Inscrição Realizada com Sucesso!')
#
#     return HttpResponseRedirect('/inscricao/')
#
#
#
# def new(request):
#     return render(request,'subscriptions/subscription_form.html', {'form':SubscriptionForm()})
#
#
# def _send_mail(subject, from_, to, template_name, context):
#
#     body = render_to_string(template_name, context)
#
#     mail.send_mail(subject, body, from_, [from_, to])
#
