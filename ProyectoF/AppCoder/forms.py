from django import forms


class TelevisorForm(forms.Form):

    marca = forms.CharField()
    tamaño = forms.IntegerField()



    