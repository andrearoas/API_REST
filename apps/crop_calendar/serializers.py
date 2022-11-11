from apps.crop_calendar.models import CropCalendar
from rest_framework import serializers


class CalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CropCalendar
        fields = (
            'id',
            'crop_start_date',
            'crop_end_date',
            'id_user',
            'id_crop',
        )
