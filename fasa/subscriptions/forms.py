from django import forms
from fasa.subscriptions.validators import validate_cpf
from django.core.exceptions import ValidationError


class SubscriptionForm(forms.Form):
    name = forms.CharField(label='nome')
    cpf = forms.CharField(label='cpf', validators=[validate_cpf])
    email = forms.EmailField(label='email', required=False)
    phone = forms.CharField(label='telefone', required=False)


    # O django sempre vai procurar um método clean ao processar um form
    # este método deve ter a assinatura clean_[nome do campo]
    # Após o django fazer a validação do método clean do CharField
    # Esta é uma forma de extender as validações de forma simples
    def clean_name(self):

        name = self.cleaned_data['name']
        words=[w.capitalize() for w in name.split()]
        return ' '.join(words)


    # Susbcrevendo o método clean do form
    # Adicionando a exception ao dicionário de erros
    def clean(self):

        #self.cleaned_data = super(SubscriptionForm, self).clean()

        if not self.cleaned_data.get('email') and \
                not self.cleaned_data.get('phone'):

            raise ValidationError('Informe seu Email ou Telefone')

        return self.cleaned_data