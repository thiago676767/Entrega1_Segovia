from django.shortcuts import render
from AppCoder.forms import TelevisorForm
from AppCoder.models import Televisores
from django.http import HttpResponse
from django.template import Template, Context


def televisorForm(request):
    if request.method == 'POST':

        miFormulario = TelevisorForm(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data

            televisor = Televisores(marca=informacion['marca'], tamaño=informacion['tamaño'])

            televisor.save() 

            return render(request, "AppCoder/inicio.html")
    else:

        miFormulario = TelevisorForm()

    return render(request, "AppCoder/telFormulario.html", {"miFormulario":miFormulario})



def TelvTemplate(self):

    miHtml = open("C:/Users/User/Desktop/coder/django/ProyectoFinal/ProyectoF/AppCoder/templates/AppCoder/telFormulario.html")

    plantilla = Template(miHtml.read())

    miHtml.close()

    miContexto = Context()

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)