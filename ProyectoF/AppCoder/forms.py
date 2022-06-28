from django import forms


class TelevisorForm(forms.Form):

    marca = forms.CharField()
    tamaño = forms.IntegerField()

class AuricularesForm(forms.Form):

    marca = forms.CharField()
    Formato = forms.CharField()

class TelefonoForm(forms.Form):
    marca = forms.CharField()
    modelo = forms.CharField()
    Tipos = forms.CharField()
    color = forms.CharField()
    precio = forms.FloatField()

    