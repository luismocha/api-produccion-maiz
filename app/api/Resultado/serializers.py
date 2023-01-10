from rest_framework import serializers
from app.models import Resultado
#from app.api.Parroquia.serializers import ParroquiaSerializer

#libreria de serealizaon de datos para mapear en la api
class ResultadoSerializer(serializers.ModelSerializer):
    #parroquiaslist=ParroquiaSerializer(many=True,read_only=True)

    class Meta:
        model = Resultado
        fields = '__all__'
    """     id= serializers.IntegerField(read_only=True)
        nombre= serializers.CharField(required=True)
        latitud= serializers.CharField(required=True)
        longitud= serializers.CharField(required=True)
        activo= serializers.BooleanField() """

    def create(self,validated_data):
        return Resultado.objects.create(**validated_data)
"""     def update(self,instancia,validated_data):
        instancia.nombre=validated_data.get('nombre',instancia.nombre)
        instancia.latitud=validated_data.get('latitud',instancia.latitud)
        instancia.longitud=validated_data.get('longitud',instancia.longitud)
        instancia.activo=validated_data.get('activo',instancia.activo)
        instancia.save()
        return instancia """
