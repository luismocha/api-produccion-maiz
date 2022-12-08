from django.db import models

# Create your models here.

class Canton(models.Model):
    nombre=models.CharField(max_length=100,unique=True)
    latitud=models.CharField(max_length=250)
    longitud=models.CharField(max_length=250)
    activo=models.BooleanField(default=True)
    """     created=models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True) """
#indice de cada recorde que se graba , la columna que se va a desplegar en el admistration
    def __str__(self) :
        return self.nombre

class Productor(models.Model):
    nombre=models.CharField(max_length=250)
    apellido=models.CharField(max_length=250)
    cedula=models.CharField(max_length=11,unique=True)
    celular=models.CharField(max_length=15)
    activo=models.BooleanField(default=True)
    fk_canton=models.ForeignKey(Canton,on_delete=models.CASCADE,related_name='canton_productor')
    """     created=models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True) """
    def __str__(self) :
        return self.nombre

class Parroquia(models.Model):
    nombre=models.CharField(max_length=100,unique=True)
    fk_canton = models.ForeignKey(Canton,on_delete=models.CASCADE,related_name='canton_parroquia')
    activo=models.BooleanField(default=True)
    """     created=models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True) """
    def __str__(self) :
        return self.nombre