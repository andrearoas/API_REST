from django.db import models
from apps.neighbour.choices import neighbours
from apps.crop.models import Crop


# neighbours model creation

class Neighbour(models.Model):
    id = models.BigAutoField(primary_key=True)
    type_neighbour = models.CharField(max_length=30, choices=neighbours, default='B')
    description_neigh = models.TextField(max_length=600)
    id_crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
