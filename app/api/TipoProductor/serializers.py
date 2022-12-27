from rest_framework import serializers
from app.models import Tipo_Productor
#from app.api.Parroquia.serializers import ParroquiaSerializer

#libreria de serealizaon de datos para mapear en la api
class TipoProductorSerializer(serializers.ModelSerializer):
    #parroquiaslist=ParroquiaSerializer(many=True,read_only=True)

    class Meta:
        model = Tipo_Productor
        fields = ['id', 'nombre']