from django.db import models

# Create your models here.
class Categoria (models.Model):
    nombre      = models.CharField(max_length = 100)
    descripcion = models.TextField(max_length = 500)

    def __str__ (self):
        return self.nombre

class Marca (models.Model):
    nombre      = models.CharField(max_length = 100)

    def __str__ (self):
        return self.nombre

class Producto (models.Model):
    nombre      = models.CharField(max_length = 100)
    descripcion = models.TextField(max_length = 500)
    estado      = models.BooleanField(default = True)
    precio      = models.DecimalField(max_digits = 6, decimal_places = 2) # 9999.99
    stock       = models.IntegerField()
    marca       = models.ForeignKey(Marca, on_delete = models.PROTECT)
    categorias  = models.ManyToManyField(Categoria, null= True, blank=True )
    def __str__ (self):
        return self.nombre + ' ' + str(self.estado)