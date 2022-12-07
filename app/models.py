from django.db import models

# Create your models here.
class Canton(models.Model):
    nombre=models.CharField(max_length=250)
    latitud=models.CharField(max_length=250)
    longitud=models.CharField(max_length=250)
    activo=models.BooleanField(default=True)
#indice de cada recorde que se graba , la columna que se va a desplegar en el admistration
    def __str__(self) :
        return self.nombre