from rest_framework import serializers
#libreria de serealizaon de datos para mapear en la api
class CantonSerializer(serializers.Serializer):
    id= serializers.IntegerField(read_only=True)
    nombre= serializers.CharField()
    latitud= serializers.CharField()
    longitud= serializers.CharField()
    activo= serializers.BooleanField()
    pass