from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Propiedad, Datos
from .form import PropiedadForm, DatosForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')
def propiedades(request):
    propiedades = Propiedad.objects.all()
    return render(request, 'builds/index.html', {'propiedades': propiedades})
def crear_propiedad(request):
    formulario = PropiedadForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('propiedades')
    return render(request, 'builds/crear.html', {'formulario': formulario})
def editar_propiedad(request,id):
    propiedad = Propiedad.objects.get(id=id)
    formulario = PropiedadForm(request.POST or None, instance=propiedad)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('propiedades')
    return render(request,'builds/editar.html',{'formulario':formulario})

def eliminar(request, id):
    propiedad = Propiedad.objects.get(id=id)
    propiedad.delete()
    return redirect('propiedades')

def login(request):
    return render(request, 'paginas/login.html', name='login')

def salir(request):
    logout(request)
    return redirect('/')

def propuser(request):
    propiedades = Propiedad.objects.all()
    return render(request, 'paginas/propiedades.html', {'propiedades': propiedades})

def agenda(request, id):
    propiedades = Propiedad.objects.get(id=id)
    formulario = DatosForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('propiedades')
    return render(request, 'builds/agenda.html', {'formulario': formulario})

def agendados(request):
    datos = Datos.objects.all()
    return render(request, 'paginas/agendados.html', {'datos':datos})

def eliminarDatos(request, id):
    datoss = Datos.objects.get(id=id)
    datoss.delete()
    return redirect('agendados')


@login_required
def index (request):
    return render(request, 'builds/index.html')

