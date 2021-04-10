from django import forms
from django.contrib.auth.models import User
from .models import *

class agregar_producto_form (forms.ModelForm):
    class Meta:
        model = Producto
        fields= '__all__'
        #fields= ['nombre', 'precio', 'marca']
        #exclude= ['nombre', 'precio', 'marca']
