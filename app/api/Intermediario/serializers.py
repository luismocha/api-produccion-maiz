from rest_framework import serializers

from app.models import Intermediario
#from app.api.Parroquia.serializers import ParroquiaSerializer

#libreria de serealizaon de datos para mapear en la api
class IntermediarioSerializer(serializers.ModelSerializer):
    #parroquiaslist=ParroquiaSerializer(many=True,read_only=True)

    class Meta:
        model = Intermediario
        fields = '__all__'
    def create(self,validated_data):
        return Intermediario.objects.create(**validated_data)
    def update(self,instancia,validated_data):
        instancia.lugar=validated_data.get('lugar',instancia.lugar)
        instancia.activo=validated_data.get('activo',instancia.activo)
        instancia.save()
        return instancia
