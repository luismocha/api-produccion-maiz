from rest_framework import serializers
from app.models import  Publicaciones
class PublicacionesSerializer(serializers.ModelSerializer):
    archivo=serializers.FileField(required=False)
    class Meta:
        model = Publicaciones
        fields = ['id','nombre','archivo','descripcion']

    def create(self,validated_data):
        return Publicaciones.objects.create(**validated_data)
    
    def update(self,instancia,validated_data):
        if(instancia.archivo):
            instancia.nombre=validated_data.get('nombre',instancia.nombre)
            instancia.archivo=validated_data.get('archivo',instancia.imagen)
            instancia.descripcion=validated_data.get('descripcion',instancia.descripcion)
            instancia.save()
            return instancia
        instancia.archivo=None
        instancia.nombre=validated_data.get('nombre',instancia.nombre)
        instancia.descripcion=validated_data.get('descripcion',instancia.descripcion)
        instancia.save()
        return instancia