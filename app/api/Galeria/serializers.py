from rest_framework import serializers
from app.models import Galeria
class GaleriaSerializer(serializers.ModelSerializer):
    imagen=serializers.ImageField(required=False)
    class Meta:
        model = Galeria
        fields = ['id','nombre','imagen','descripcion']

    def create(self,validated_data):
        return Galeria.objects.create(**validated_data)
    
    def update(self,instancia,validated_data):
        if(instancia.imagen):
            instancia.nombre=validated_data.get('nombre',instancia.nombre)
            instancia.imagen=validated_data.get('imagen',instancia.imagen)
            instancia.descripcion=validated_data.get('descripcion',instancia.descripcion)
            instancia.save()
            return instancia
        instancia.imagen=None
        instancia.nombre=validated_data.get('nombre',instancia.nombre)
        instancia.descripcion=validated_data.get('descripcion',instancia.descripcion)
        instancia.save()
        return instancia