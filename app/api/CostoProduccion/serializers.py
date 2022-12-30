from rest_framework import serializers
from app.models import  Costo_Produccion
#from app.api.Parroquia.serializers import ParroquiaSerializer

#libreria de serealizaon de datos para mapear en la api
class CostoProduccionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Costo_Produccion
        fields = '__all__'

    def create(self,validated_data):
        return Costo_Produccion.objects.create(**validated_data)
"""     def update(self,instancia,validated_data):
        instancia.nombre=validated_data.get('nombre',instancia.nombre)
        instancia.latitud=validated_data.get('latitud',instancia.latitud)
        instancia.longitud=validated_data.get('longitud',instancia.longitud)
        instancia.activo=validated_data.get('activo',instancia.activo)
        instancia.save()
        return instancia  """
