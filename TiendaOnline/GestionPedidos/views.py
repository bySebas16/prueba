from django.shortcuts import render
from django.http import HttpResponse
from GestionPedidos.models import Articulos
from django.core.mail import send_mail
from django.conf import settings
from GestionPedidos.forms import FormularioContacto

# Create your views here.

def busqueda_productos(request):
    return render(request, "busqueda_productos.html")

def buscar(request):
    #mira si has introducido algo
    if request.GET["prd"]:

        producto=request.GET["prd"]

        if len(producto)>20:

            mensaje="Texto de busqueda demasiado largo"

        else: 

            articulos = Articulos.objects.filter(nombre__icontains=producto) #filtra por el nombre del producto (que tenga incluida esa palabra en el nombre)

            return render(request, "resultados_busqueda.html", {"articulos":articulos, "query":producto})

    else:
        mensaje="No has introducido nada"

    return HttpResponse(mensaje)


def contacto(request):

    if request.method == "POST":
        
        miFormulario=FormularioContacto(request.POST)

        if miFormulario.is_valid():
            infForm=miFormulario.cleaned_data

            send_mail(infForm['asunto'], infForm['mensaje'],
            infForm.get('email', ''), ['bysebas16@gmail.com'],)

            return render(request, "contacto.html")

    else:
        miFormulario = FormularioContacto()

    return render(request, "formulario_contacto.html", {"form":miFormulario})