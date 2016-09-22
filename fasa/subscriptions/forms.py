from django import forms


class SubscriptionForm(forms.Form):
    name = forms.CharField(label='nome')
    cpf = forms.CharField(label='cpf')
    email = forms.EmailField(label='email')
    phone = forms.CharField(label='telefone')