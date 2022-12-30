from rest_framework import serializers
from app.api.Intermediario.serializers import IntermediarioSerializer
from app.api.Produccion.serializer import ProduccionSerializer
from app.models import Intermediario, Intermediario_Produccion, Produccion
#from app.api.Canton.serializers import CantonSerializer
#from app.api.Canton.serializers import CantonSerializer
#from app.api.Canton.serializers import CantonSerializer
#libreria de serealizaon de datos para mapear en la api

class IntermediarioProduccionSerializer(serializers.ModelSerializer):
    #produccion = ProduccionSerializer(read_only=True, many=True)
    fk_intermediario=IntermediarioSerializer(read_only=True)
    fk_intermediario_id=serializers.SlugRelatedField(queryset=Intermediario.objects.all(),slug_field='id', write_only=True)
        
    fk_produccion=ProduccionSerializer(read_only=True)
    fk_produccion_id=serializers.SlugRelatedField(queryset=Produccion.objects.all(),slug_field='id', write_only=True)

    class Meta:
        model = Intermediario_Produccion
        fields = [
            'fk_intermediario',
            'fk_intermediario_id',
            'fk_produccion',
            'fk_produccion_id',
            'year_compra',
            'cantidad_comprada',
            'activo',
        ]
        
    
"""     def create(self, validated_data):
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
        return instancia  """