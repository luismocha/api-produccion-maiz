from rest_framework import serializers
from app.api.Lugar.serializers import LugarSerializer
from app.models import Intermediario, Lugar
#from app.api.Canton.serializers import CantonSerializer
#from app.api.Canton.serializers import CantonSerializer
#from app.api.Canton.serializers import CantonSerializer
#libreria de serealizaon de datos para mapear en la api

class IntermediarioSerializer(serializers.ModelSerializer):
    fk_lugar=LugarSerializer(read_only=True)
    fk_lugar_id=serializers.SlugRelatedField(queryset=Lugar.objects.all(),slug_field='id', write_only=True)

    class Meta:
        model = Intermediario
        fields = ['id','year_compra', 'cantidad_comprada', 'activo', 'fk_lugar','fk_lugar_id']

    
    def create(self, validated_data):
        data = {
                'year_compra': validated_data.get('year_compra', None),
                'cantidad_comprada': validated_data.get('cantidad_comprada', None),
                'activo': validated_data.get('activo', None),
                'fk_lugar': validated_data.get('fk_lugar_id', None)
                }
        return Intermediario.objects.create(**data)

    def update(self,instancia,validated_data):
        instancia.year_compra=validated_data.get('year_compra',instancia.year_compra)
        instancia.cantidad_comprada=validated_data.get('cantidad_comprada',instancia.cantidad_comprada)
        instancia.activo=validated_data.get('activo',instancia.activo)
        instancia.fk_lugar=validated_data.get('fk_lugar_id',instancia.fk_lugar)
        instancia.save()
        return instancia 