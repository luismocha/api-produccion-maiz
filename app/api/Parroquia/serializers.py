from rest_framework import serializers
from app.api.Canton.serializers import CantonSerializer
#from app.api.Canton.serializers import CantonSerializer
#from app.api.Canton.serializers import CantonSerializer
#from app.api.Canton.serializers import CantonSerializer
from app.models import Canton, Parroquia
#libreria de serealizaon de datos para mapear en la api

class ParroquiaSerializer(serializers.ModelSerializer):
    fk_canton=CantonSerializer(read_only=True)
    fk_canton_id=serializers.SlugRelatedField(queryset=Canton.objects.all(),slug_field='id', write_only=True)

    class Meta:
        model = Parroquia
        fields = ['id','nombre', 'fk_canton', 'fk_canton_id', 'activo']
        #fields = ['canton_nombre']
        #fields = ('id', 'nombre', 'canton_nombre')
        #read_only_fields = ('canton_nombre')
        #fields = ('canton_nombre')
        #exclude = ('canton_nombre')
    #id= serializers.IntegerField(read_only=True)
    #nombre= serializers.CharField()
    #fk_canton= serializers.PrimaryKeyRelatedField( many=False,queryset=Canton.objects.all(), write_only=True)
    #fk_canton= serializers.IntegerField()
    #activo= serializers.BooleanField()
    
    def create(self, validated_data):
        print("xxxxxxxxxxx")
        print(validated_data)
        data = {
                'nombre': validated_data.get('nombre', None),
                'fk_canton': validated_data.get('fk_canton_id', None),
                'activo': validated_data.get('activo', None)
                }
        return Parroquia.objects.create(**data)

    def update(self,instancia,validated_data):
        instancia.nombre=validated_data.get('nombre',instancia.nombre)
        instancia.fk_canton=validated_data.get('fk_canton',instancia.fk_canton)
        instancia.activo=validated_data.get('activo',instancia.activo)
        instancia.save()
        return instancia 