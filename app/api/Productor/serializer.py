from rest_framework import serializers
#from app.api.Parroquia.serializers import ParroquiaSerializer
#from app.api.Canton.serializers import CantonSerializer
from app.models import   Productor,Canton,Parroquia
#libreria de serealizaon de datos para mapear en la api
from app.api.Canton.serializers import CantonSerializer
from app.api.Parroquia.serializers import ParroquiaSerializer

class ProductorSerializer(serializers.ModelSerializer):
    ##parroquiaslist=ParroquiaSerializer(many=True,read_only=True)
    fk_canton=CantonSerializer(read_only=True)
    fk_canton_id=serializers.SlugRelatedField(queryset=Canton.objects.all(),slug_field='id', write_only=True)
    
    fk_parroquia=ParroquiaSerializer(read_only=True)
    fk_parroquia_id=serializers.SlugRelatedField(queryset=Parroquia.objects.all(),slug_field='id', write_only=True)
    #parroquia_nombre=serializers.CharField(source='Parroquia.nombre',read_only=True)
    class Meta:
        model = Productor
        fields = [
        'id',
        'nombre',
        'apellido',
        'cedula',
        'celular',
        'fk_canton', 
        'fk_canton_id', 
        'fk_parroquia',
        'fk_parroquia_id',
        'activo']
        #fields = '__all__'
    """     id= serializers.IntegerField(read_only=True)
        nombre= serializers.CharField()
        fk_canton= serializers.PrimaryKeyRelatedField( many=False,queryset=Canton.objects.all()) """
    #fk_canton= CantonSerializer(many=True,read_only=True)
    #activo= serializers.BooleanField()
    
    def create(self, validated_data):
        data={
            'nombre': validated_data.get('nombre',None),
            'apellido': validated_data.get('apellido',None),
            'cedula': validated_data.get('cedula',None),
            'celular': validated_data.get('celular',None),
            'activo': validated_data.get('activo',None),
            "fk_canton": validated_data.get('fk_canton_id',None),
            "fk_parroquia": validated_data.get('fk_parroquia_id',None),
        }
        return Productor.objects.create(**data)

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