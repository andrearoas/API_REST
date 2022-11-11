from django.db import models
from apps.users.models import User
from apps.category.models import Category
from apps.crop.choices import container


# Create your models here.


class Crop(models.Model):
    id = models.BigAutoField(primary_key=True)
    photo_crop = models.ImageField(upload_to='image_crops')
    name_crop = models.CharField(max_length=30)
    name_scie_crop = models.CharField(max_length=30)
    description_crop = models.TextField(max_length=600)
    time_germination = models.PositiveSmallIntegerField()
    time_harvest = models.PositiveSmallIntegerField(default=8)
    time_seeding = models.CharField(max_length=15)
    time_sun_crop = models.CharField(max_length=20)
    amount_water_crop = models.CharField(max_length=30)
    distance_crops = models.PositiveSmallIntegerField()
    height_max_crop = models.PositiveSmallIntegerField()
    type_container = models.CharField(max_length=30, choices=container, default='Ma')
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    id_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
