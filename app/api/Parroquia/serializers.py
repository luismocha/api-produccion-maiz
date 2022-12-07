from rest_framework import serializers
from app.api.serializers import CantonSerializer
from app.models import Canton, Parroquia
#libreria de serealizaon de datos para mapear en la api

class ParroquiaSerializer(serializers.Serializer):
    class Meta:
        model = Parroquia
        fields = '__all__'
    id= serializers.IntegerField(read_only=True)
    nombre= serializers.CharField()
    fk_canton= serializers.PrimaryKeyRelatedField( many=False,queryset=Canton.objects.all())
    #fk_canton= CantonSerializer(many=True,read_only=True)
    activo= serializers.BooleanField()
    
    def create(self, validated_data):
        print("xxxxxxxxxxx")
        print(validated_data)
        return Parroquia.objects.create(**validated_data)

    def update(self,instancia,validated_data):
        instancia.nombre=validated_data.get('nombre',instancia.nombre)
        instancia.fk_canton=validated_data.get('fk_canton',instancia.fk_canton)
        instancia.activo=validated_data.get('activo',instancia.activo)
        instancia.save()
        return instancia 