from rest_framework import serializers
from apps.crop.models import Crop


class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crop
        fields = (
            'id',
            'photo_crop',
            'name_crop',
            'name_scie_crop',
            'description_crop',
            'time_germination',
            'time_harvest',
            'time_seeding',
            'time_sun_crop',
            'amount_water_crop',
            'distance_crops',
            'height_max_crop',
            'type_container',
            'id_user',
            'id_category',
        )
        # read_only_fields = (
        #      'id_user',
        #      'id_category',
        #     )
