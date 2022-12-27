from django.db import models
import datetime
# Create your models here.
class Canton(models.Model):
    nombre=models.CharField(max_length=100,unique=True)
    latitud=models.CharField(max_length=250)
    longitud=models.CharField(max_length=250)
    activo=models.BooleanField(default=True)
    """     created=models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)  """
#indice de cada recorde que se graba , la columna que se va a desplegar en el admistration
    def __str__(self) :
        return self.nombre

class Parroquia(models.Model):
    nombre=models.CharField(max_length=100,unique=True)
    fk_canton = models.ForeignKey(Canton,on_delete=models.RESTRICT,related_name='parroquiaslist')
    activo=models.BooleanField(default=True)
    """     created=models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)  """
    def __str__(self) :
        return self.nombre

class Productor(models.Model):
    nombre=models.CharField(max_length=250)
    apellido=models.CharField(max_length=250)
    cedula=models.CharField(max_length=11,unique=True)
    celular=models.CharField(max_length=15)
    activo=models.BooleanField(default=True)
    fk_canton=models.ForeignKey(Canton,on_delete=models.RESTRICT,related_name='cantonlist')
    fk_parroquia=models.ForeignKey(Parroquia,on_delete=models.RESTRICT,related_name='parroquialist')
    """     created=models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)  """
    def __str__(self) :
        return self.nombre

class Tipo_Productor(models.Model):
    nombre=models.CharField(max_length=100,unique=True)
    def __str__(self) :
        return self.nombre

class Produccion(models.Model):
    year =models.PositiveIntegerField(max_length=4)
    hectarias=models.DecimalField(max_digits=19, decimal_places=2)
    precio_venta=models.DecimalField(max_digits=19, decimal_places=2)
    toneladas=models.DecimalField(max_digits=19, decimal_places=2)
    quintales=models.DecimalField(max_digits=19, decimal_places=2)
    activo=models.BooleanField(default=True)
    fk_tipo_productor=models.ForeignKey(Tipo_Productor,on_delete=models.RESTRICT,related_name='tipoproductorlist')
    fk_productor=models.ForeignKey(Productor,on_delete=models.RESTRICT,related_name='listarproductoresproduccion')
    def __str__(self) :
        return str(self.year)



