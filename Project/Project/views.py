from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader
from django.template.loader import get_template
from django.shortcuts import render


class Persona(object):

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

def saludos(request): #vista
    persona = Persona("Sebastian", "Idarraga")
    temas = ["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue de la aplicacion"]

    #doc_externo = loader.get_template("plantilla.html")
    #documento = doc_externo.render({"nombre_persona": persona.nombre, "apellido_persona": persona.apellido, "temas":temas})

    return render(request, "plantilla.html", {"nombre_persona": persona.nombre, "apellido_persona": persona.apellido, "temas":temas})

def cursoC(request):
    fecha_actual = datetime.datetime.now()

    return render(request, "cursoC.html", {"dameFecha":fecha_actual})

def cursoCss(request):
    persona = Persona("Sebastian", "Idarraga")

    return render(request, "cursoCss.html", {"nombre_persona": persona.nombre, "apellido_persona": persona.apellido})

def fecha(request):
    fecha_actual = datetime.datetime.now()
    documento = """<html>
    <body>
    <h1>
    Fecha y horas actuales %s
    </h1>
    </body>
    </html>"""% fecha_actual

    return HttpResponse(documento)

def calculoEdad(request, edad, year):
    periodo = year - 2020
    edadF = edad + periodo
    documento = "En el año %s tendras %s años" %(year, edadF)

    return HttpResponse(documento)
