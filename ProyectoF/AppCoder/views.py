from django.shortcuts import render
from AppCoder.forms import TelevisorForm, AuricularesForm, TelefonoForm
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

def auricularesForm(request):
    if request.method == 'POST':

        miFormulario = AuricularesForm(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data

            auricular = Auriculares(marca=informacion['marca'], formato=informacion['formato'])

            auricular.save() 

            return render(request, "AppCoder/inicio.html")
    else:

        miFormulario = AuricularesForm()

    return render(request, "AppCoder/auriFormulario.html", {"miFormulario":miFormulario})

def telefonoForm(request):
    if request.method == 'POST':

        miFormulario = TelefonoForm(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data

            telefono = Telefonos(marca=informacion['marca'], modelo=informacion['modelo'], Tipos=informacion['Tipos'], color=informacion['color'], precio=informacion['precio'])

            telefono.save() 

            return render(request, "AppCoder/inicio.html")
    else:

        miFormulario = TelefonoForm()

    return render(request, "AppCoder/telefonoFormulario.html", {"miFormulario":miFormulario})





def TelvTemplate(self):

    miHtml = open("C:/Users/User/Desktop/coder/django/ProyectoFinal/ProyectoF/AppCoder/templates/AppCoder/telFormulario.html")

    plantilla = Template(miHtml.read())

    miHtml.close()

    miContexto = Context()

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)


def TelefTemplate(self):

    miHtml = open("C:/Users/User/Desktop/coder/django/ProyectoFinal/ProyectoF/AppCoder/templates/AppCoder/telefonoFormulario.html")

    plantilla = Template(miHtml.read())

    miHtml.close()

    miContexto = Context()

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)


def AuriTemplate(self):

    miHtml = open("C:/Users/User/Desktop/coder/django/ProyectoFinal/ProyectoF/AppCoder/templates/AppCoder/auriFormulario.html")

    plantilla = Template(miHtml.read())

    miHtml.close()

    miContexto = Context()

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)