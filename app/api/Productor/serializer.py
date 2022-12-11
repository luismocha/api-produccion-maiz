from rest_framework import serializers
from app.api.Canton.serializers import CantonSerializer
from app.models import  Parroquia, Productor
#libreria de serealizaon de datos para mapear en la api

class ProductorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productor
        fields = '__all__'
    """     id= serializers.IntegerField(read_only=True)
        nombre= serializers.CharField()
        fk_canton= serializers.PrimaryKeyRelatedField( many=False,queryset=Canton.objects.all()) """
    #fk_canton= CantonSerializer(many=True,read_only=True)
    #activo= serializers.BooleanField()
    
    def create(self, validated_data):
        print("xxxxxxxxxxx")
        print(validated_data)
        return Productor.objects.create(**validated_data)

    def update(self,instancia,validated_data):
        instancia.nombre=validated_data.get('nombre',instancia.nombre)
        instancia.apellido=validated_data.get('apellido',instancia.apellido)
        instancia.cedula=validated_data.get('cedula',instancia.cedula)
        instancia.celular=validated_data.get('celular',instancia.celular)
        instancia.fk_canton=validated_data.get('fk_canton',instancia.fk_canton)
        instancia.activo=validated_data.get('activo',instancia.activo)
        instancia.fk_parroquia=validated_data.get('fk_parroquia',instancia.fk_parroquia)
        instancia.save()
        return instancia 