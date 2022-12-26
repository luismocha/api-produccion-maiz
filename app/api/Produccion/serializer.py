from rest_framework import serializers
from app.api.Productor.serializer import ProductorSerializer
from app.api.TipoProductor.serializers import TipoProductorSerializer

from app.models import Produccion, Productor, Tipo_Productor


class ProduccionSerializer(serializers.ModelSerializer):
    fk_productor=ProductorSerializer(read_only=True)
    fk_productor_id=serializers.SlugRelatedField(queryset=Productor.objects.all(),slug_field='id', write_only=True)
    
    fk_tipo_productor=TipoProductorSerializer(read_only=True)
    fk_tipo_productor_id=serializers.SlugRelatedField(queryset=Tipo_Productor.objects.all(),slug_field='id', write_only=True)
    class Meta:
        model:Produccion
        fields = ['id','year', 'costo_total', 'precio_venta', 'toneladas','quintales','activo','fk_tipo_productor_id','fk_productor_id']
    def create(self, validated_data):
        data = {
                'year': validated_data.get('year', None),
                'costo_total': validated_data.get('costo_total', None),
                'precio_venta': validated_data.get('precio_venta', None),
                'toneladas': validated_data.get('toneladas', None),
                'quintales': validated_data.get('quintales', None),
                'activo': validated_data.get('activo', None),
                'fk_tipo_productor': validated_data.get('fk_tipo_productor_id', None),
                'fk_productor': validated_data.get('fk_productor_id', None),
                }
        return Produccion.objects.create(**data)