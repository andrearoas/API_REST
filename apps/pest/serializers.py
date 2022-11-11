from rest_framework import serializers
from apps.pest.models import Pest


class PestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pest
        fields = (
            'id',
            'name_pest',
            'description_pest',
            'photo_pest',
            'description_prevent',
            'id_crop',
        )
