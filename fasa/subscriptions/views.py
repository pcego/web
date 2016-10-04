from django.shortcuts import render

from fasa.subscriptions.forms import SubscriptionForm
from django.template.loader import render_to_string
from django.core import mail
from django.http import HttpResponseRedirect
from django.contrib import messages


def subscribe(request):

    ## Verifica se o método da requisição é POST
    if request.method == 'POST':
        ## Atribue a variável form os dados vindos do formulário
        form = SubscriptionForm(request.POST)

        ## Método que trata os dados recebidos do formulário
        ## e os converte para objetos python de alto nível
        ## aplicando o metodo full_clean() no processo
        if form.is_valid():

            ## O método cleaned_data cria um dicionário
            ## com o dados já tratados pelo full_clean()
            data = form.cleaned_data
            body = render_to_string('subscriptions/subscription_email.txt',
                                    data)

            mail.send_mail('Confirmação de Incrição.',
                           body,
                           'contato@fasa.edu.br',
                           ['contato@fasa.edu.br', data['email']])

            messages.success(request, 'Inscrição Realizada com Sucesso!')

            return HttpResponseRedirect('/inscricao/')

        else:
            return render(request, 'subscriptions/subscription_form.html',
                          {'form': form})


    else:
        context = {'form':SubscriptionForm()}
        return render(request,'subscriptions/subscription_form.html', context)
