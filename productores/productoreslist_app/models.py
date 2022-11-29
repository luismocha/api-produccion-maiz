from django.db import models

# Create your models here.
class Productor(models.Model):
    nombre=models.CharField(max_length=50)
    cedula=models.CharField(max_length=11)
    apellido=models.CharField(max_length=50)
    celular=models.CharField(max_length=12)
    estado=models.BooleanField(default=True)
    #fk_canto:
    #columna a mostrar en el django adminstrator
    def __str__(self) :
        return self.nombre