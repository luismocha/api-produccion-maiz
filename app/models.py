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
    hectareas=models.DecimalField(max_digits=19, decimal_places=2)
    precio_venta=models.DecimalField(max_digits=19, decimal_places=2)
    toneladas=models.DecimalField(max_digits=19, decimal_places=2)
    quintales=models.PositiveIntegerField()
    activo=models.BooleanField(default=True)
    fk_tipo_productor=models.ForeignKey(Tipo_Productor,on_delete=models.RESTRICT,related_name='tipoproductorlist')
    fk_productor=models.ForeignKey(Productor,on_delete=models.RESTRICT,related_name='listarproductoresproduccion')
    stock=models.PositiveIntegerField()
    def __str__(self) :
        return str(self.year)


class Intermediario(models.Model):
    lugar=models.CharField(max_length=100,unique=True)
    activo=models.BooleanField(default=True)
    def __str__(self) :
        return self.lugar
        
##tabla relacional personalizada de many to many
class Intermediario_Produccion(models.Model):
    fk_intermediario=models.ForeignKey(Intermediario,on_delete=models.RESTRICT, blank=True, 
        null=True)
    fk_produccion=models.ForeignKey(Produccion,on_delete=models.RESTRICT, blank=True, 
        null=True)
    year_compra =models.PositiveIntegerField(max_length=4)
    cantidad_comprada=models.PositiveIntegerField()
    activo=models.BooleanField(default=True)
    def __str__(self) :
        return str(self.year_compra)+" "+str(self.cantidad_comprada)


class Costo_Produccion(models.Model):
    year =models.PositiveIntegerField(max_length=4,unique=True)
    costo_total=models.DecimalField(max_digits=19, decimal_places=2)
    activo=models.BooleanField(default=True)

    ##cosecha
    recolectado=models.DecimalField(max_digits=19, decimal_places=2)
    amontonado=models.DecimalField(max_digits=19, decimal_places=2)
    desgranado=models.DecimalField(max_digits=19, decimal_places=2)
    alquiler_desgranadora=models.DecimalField(max_digits=19, decimal_places=2)
    ensacado_almacenamiento=models.DecimalField(max_digits=19, decimal_places=2)
    control_tratamiento_maiz=models.DecimalField(max_digits=19, decimal_places=2)
    venta=models.DecimalField(max_digits=19, decimal_places=2)
    cosecha_total=models.DecimalField(max_digits=19, decimal_places=2)

    ##labores culturales
    primera_fertilizacion=models.DecimalField(max_digits=19, decimal_places=2)
    primer_control_plagas=models.DecimalField(max_digits=19, decimal_places=2)
    primer_control_enfermedades=models.DecimalField(max_digits=19, decimal_places=2)
    aplicacion_hebricida=models.DecimalField(max_digits=19, decimal_places=2)
    segunda_fertilizacion=models.DecimalField(max_digits=19, decimal_places=2)
    segundo_control_plagas=models.DecimalField(max_digits=19, decimal_places=2)
    segundo_control_enfermedades=models.DecimalField(max_digits=19, decimal_places=2)
    tercera_fertilizacion=models.DecimalField(max_digits=19, decimal_places=2)
    tiempo_espera=models.DecimalField(max_digits=19, decimal_places=2)
    labores_culturales_total=models.DecimalField(max_digits=19, decimal_places=2)
   
    ##siembra
    desbroce_monte=models.DecimalField(max_digits=19, decimal_places=2)
    quema_maleza=models.DecimalField(max_digits=19, decimal_places=2)
    seleccion_semilla=models.DecimalField(max_digits=19, decimal_places=2)
    aplicacion_herbicida=models.DecimalField(max_digits=19, decimal_places=2)
    desinfeccion_semilla=models.DecimalField(max_digits=19, decimal_places=2)
    siembra=models.DecimalField(max_digits=19, decimal_places=2)
    siembra_total=models.DecimalField(max_digits=19, decimal_places=2)
    
    def __str__(self) :
        return str(self.desbroceMonte)+" "+str(self.quemaMaleza)

class Resultado(models.Model):
    year =models.PositiveIntegerField(max_length=4,unique=True)
    costo_total_produccion=models.DecimalField(max_digits=19, decimal_places=2)
    rentabilidad=models.DecimalField(max_digits=19, decimal_places=2)
    def __str__(self) :
        return str(self.year)+" "+str(self.costo_total_produccion)+" "+str(self.rentabilidad)
