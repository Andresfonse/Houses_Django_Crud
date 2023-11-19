from django.db import models

# Create your models here.
class Propiedad(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=180, verbose_name='Titulo')
    imagen = models.TextField( null=True, verbose_name='Imagen')
    description = models.TextField(null=True,  verbose_name='Descripcion')
    precio = models.IntegerField(null=True, verbose_name='precio')

    def __str__(self):
        fila = "Titulo: "+ self.titulo + "-" + "Descripcion:" + self.description
        return fila

class Datos(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=180, verbose_name='Nombre')
    apellidos = models.TextField(null=True, verbose_name='Apellido')
    telefono = models.IntegerField(null=True, verbose_name='Telefono')


