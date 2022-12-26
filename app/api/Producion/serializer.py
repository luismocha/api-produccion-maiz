from rest_framework import serializers

from app.models import Produccion


class ProduccionSerializer(serializers.ModelSerializer):
    class Meta:
        model:Produccion