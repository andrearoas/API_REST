from abc import ABC
from rest_framework import serializers
from apps.crop.models import Crop, Crop2


# from apps.users.serializers import UserSerializer


class CropSerializer(serializers.ModelSerializer):
    # id_user = serializers.StringRelatedField()
    # id_category = serializers.StringRelatedField()

    class Meta:
        model = Crop
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'photo_crop': instance.photo_crop if instance.photo_crop != '' else '',
            'name_crop': instance.name_crop,
            'name_scie_crop': instance.name_scie_crop,
            'description_crop': instance.description_crop,
            'time_germination': instance.time_germination,
            'time_harvest': instance.time_harvest,
            'time_seeding': instance.time_seeding,
            'time_sun_crop': instance.time_sun_crop,
            'amount_water_crop': instance.amount_water_crop,
            'distance_crops': instance.distance_crops,
            'height_max_crop': instance.height_max_crop,
            'type_container': instance.type_container,
        }


class Crop2Serializer(serializers.Serializer):
    class Meta:
        model = Crop2
        fields = '__all__'
