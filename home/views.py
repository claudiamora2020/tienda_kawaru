from django.shortcuts import render, redirect
from .models import Producto
from .forms import*

# Create your views here.
def index_view (request) :
    return render(request, 'index.html', locals()) #pagina de inicio

def about_view (request) :
    return render(request, 'about.html', locals())

def listar_producto_view(request) :
    lista = Producto.objects.filter()
    return render(request, 'listar_producto.html', locals())

def agregar_producto_view (request) :
    if request.method == 'POST':
        formulario = agregar_producto_form(request.POST, request.FILES)
        if formulario.is_valid(): # is_valid es heredado de la clase model form
            formulario.save()     #si es valido podemos grabar
            return redirect ('/listar_producto/')
    else:
        formulario = agregar_producto_form()
    return render(request, 'agregar_producto.html', locals()) # cuando termine carga la misma lista

def ver_producto_view(request, id_prod):
    p = Producto.objects.get(id=id_prod)
    return render(request, 'ver_producto.html', locals())

def editar_producto_view(request, id_prod): 
    p = Producto.objects.get(id=id_prod)
    if request.method == 'POST':
        formulario = agregar_producto_form(request.POST, request.FILES, instance = p) #instance logra que edite
        if formulario.is_valid():
            p = formulario.save()
            return redirect ('/listar_producto/')
    else:
        formulario = agregar_producto_form(instance = p)
    return render(request, 'agregar_producto.html', locals())
    
def eliminar_producto_view(request, id_prod):
    p = Producto.objects.get(id=id_prod)
    p.delete()
    return redirect ('/listar_producto/')