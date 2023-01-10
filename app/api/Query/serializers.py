from rest_framework import serializers
from django.contrib.auth.models import User


############# ESTE ES EL Q FUNCIONA ##############
class ResultadoTablasAppSerializer(serializers.Serializer):
    #mapear la data
    year=serializers.CharField(max_length=4)
