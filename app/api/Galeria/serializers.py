from rest_framework import serializers
from app.models import Galeria
class GaleriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Galeria
        fields = '__all__'

    def create(self,validated_data):
        return Galeria.objects.create(**validated_data)
