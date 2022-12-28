from rest_framework import serializers
from app.models import  Lugar
#from app.api.Parroquia.serializers import ParroquiaSerializer

#libreria de serealizaon de datos para mapear en la api
class LugarSerializer(serializers.ModelSerializer):
    #parroquiaslist=ParroquiaSerializer(many=True,read_only=True)

    class Meta:
        model = Lugar
        fields = '__all__'
    def create(self,validated_data):
        return Lugar.objects.create(**validated_data)
    def update(self,instancia,validated_data):
        instancia.nombre=validated_data.get('nombre',instancia.nombre)
        instancia.activo=validated_data.get('activo',instancia.activo)
        instancia.save()
        return instancia
