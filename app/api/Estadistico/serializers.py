from rest_framework import serializers


############# ESTE ES EL Q FUNCIONA ##############
class EstadisticosSerializer(serializers.Serializer):
    #mapear la data
    productores=serializers.DecimalField(max_digits=19, decimal_places=2)
