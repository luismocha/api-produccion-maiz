from rest_framework import serializers
from app.models import Canton
#from app.api.Parroquia.serializers import ParroquiaSerializer

#libreria de serealizaon de datos para mapear en la api
class CantonSerializer(serializers.ModelSerializer):
    #parroquiaslist=ParroquiaSerializer(many=True,read_only=True)

    class Meta:
        model = Canton
        fields = '__all__'
    """     id= serializers.IntegerField(read_only=True)
        nombre= serializers.CharField(required=True)
        latitud= serializers.CharField(required=True)
        longitud= serializers.CharField(required=True)
        activo= serializers.BooleanField() """

    def create(self,validated_data):
        return Canton.objects.create(**validated_data)
    def update(self,instancia,validated_data):
        instancia.nombre=validated_data.get('nombre',instancia.nombre)
        instancia.latitud=validated_data.get('latitud',instancia.latitud)
        instancia.longitud=validated_data.get('longitud',instancia.longitud)
        instancia.activo=validated_data.get('activo',instancia.activo)
        instancia.save()
        return instancia
""" class CantonFkSerializer(serializers.Serializer):
    class Meta:
        model = Canton
        fields = '__all__'
    id= serializers.IntegerField(read_only=True)
    nombre= serializers.CharField()
    latitud= serializers.CharField()
    longitud= serializers.CharField()
    activo= serializers.BooleanField() """
