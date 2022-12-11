from rest_framework import serializers
from app.api.Canton.serializers import CantonSerializer
from app.models import Canton, Parroquia
#libreria de serealizaon de datos para mapear en la api

class ParroquiaSerializer(serializers.ModelSerializer):

    #fk_canton = serializers.HyperlinkedIdentityField(many=True,read_only=True,view_name='listar-cantones')
    #print('xxxxxxxxxxxx')
    ##print(fk_canton)
    #fk_canton = serializers.StringRelatedField(many=True)
    #fk_canton = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    #print(fk_canton)
    #print(canton)
    #fk_canton = serializers.SlugRelatedField(queryset=canton.objects.all(), slug_field='canton', write_only=True)
    #fk_canton= serializers.PrimaryKeyRelatedField( many=False,queryset=Canton.objects.all(), write_only=True)
    class Meta:
        model = Parroquia
        fields = '__all__'
    #id= serializers.IntegerField(read_only=True)
    #nombre= serializers.CharField()
    #fk_canton= serializers.PrimaryKeyRelatedField( many=False,queryset=Canton.objects.all(), write_only=True)
    #fk_canton= serializers.IntegerField()
    #activo= serializers.BooleanField()
    
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