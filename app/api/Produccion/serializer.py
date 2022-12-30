from rest_framework import serializers
from app.api.Productor.serializer import ProductorSerializer
from app.api.TipoProductor.serializers import TipoProductorSerializer
from app.models import Produccion, Productor, Tipo_Productor



class ProduccionSerializer(serializers.ModelSerializer):
    stock=serializers.IntegerField(read_only=True)
    #import pdb; pdb.set_trace()
    fk_productor=ProductorSerializer(read_only=True)
    fk_productor_id=serializers.SlugRelatedField(queryset=Productor.objects.all(),slug_field='id', write_only=True)
    
    fk_tipo_productor=TipoProductorSerializer(read_only=True)
    fk_tipo_productor_id=serializers.SlugRelatedField(queryset=Tipo_Productor.objects.all(),slug_field='id', write_only=True)
    
    class Meta:
        model=Produccion
        fields = [
            'id',
            'year', 
            'hectareas', 
            'precio_venta', 
            'toneladas',
            'toneladas',
            'quintales',
            'activo',
            'stock',
            'fk_productor',
            'fk_productor_id',
            'fk_tipo_productor',
            'fk_tipo_productor_id'
            ]
    def create(self, validated_data):
        data = {
                'year': validated_data.get('year', None),
                'hectareas': validated_data.get('hectareas', None),
                'precio_venta': validated_data.get('precio_venta', None),
                'toneladas': validated_data.get('toneladas', None),
                'quintales': validated_data.get('quintales', None),
                'activo': validated_data.get('activo', None),
                'stock':validated_data.get('quintales', None),
                'fk_tipo_productor': validated_data.get('fk_tipo_productor_id', None),
                'fk_productor': validated_data.get('fk_productor_id', None),
                }
        #return Produccion.objects.create(**validated_data)

        return Produccion.objects.create(**data)
    def update(self,instancia,validated_data):
        ####### REGLA NE NEFOCIO el año ni el productor no puede actulizar ##########
        #instancia.year=validated_data.get('year',instancia.year)
        instancia.hectareas=validated_data.get('hectareas',instancia.hectareas)
        instancia.precio_venta=validated_data.get('precio_venta',instancia.precio_venta)
        instancia.toneladas=validated_data.get('toneladas',instancia.toneladas)
        instancia.quintales=validated_data.get('quintales',instancia.quintales)
        instancia.activo=validated_data.get('activo',instancia.activo)
        #instancia.stock=validated_data.get('stock',instancia.stock)
        instancia.fk_tipo_productor=validated_data.get('fk_tipo_productor_id',instancia.fk_tipo_productor)
        #instancia.fk_productor=validated_data.get('fk_productor',instancia.fk_productor)
        instancia.save()
        return instancia 