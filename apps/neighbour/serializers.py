from apps.neighbour.models import Neighbour
from rest_framework import serializers


class NeighbourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neighbour
        fields = (
            'id',
            'type_neighbour',
            'description_neigh',
            'id_crop',
        )

