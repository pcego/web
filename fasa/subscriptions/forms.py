from django import forms
from fasa.subscriptions.validators import validate_cpf


class SubscriptionForm(forms.Form):
    name = forms.CharField(label='nome')
    cpf = forms.CharField(label='cpf', validators=[validate_cpf])
    email = forms.EmailField(label='email')
    phone = forms.CharField(label='telefone')


    # O django sempre vai procurar um método clean ao processar um form
    # este método deve ter a assinatura clean_[nome do campo]
    # Após o django fazer a validação do método clean do CharField
    # Esta é uma forma de extender as validações de forma simples
    def clean_name(self):

        name = self.cleaned_data['name']
        words = []

        for w in name.split():
            words.append(w.capitalize())

        capitalized_name = ' '.join(words)

        return capitalized_name

        # name = self.cleaned_data['name']
        # words=[w.capitalize() for w in name.split()]
        #
        # return ' '.join(words)