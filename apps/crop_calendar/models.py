from django.db import models
from apps.users.models import User
from apps.crop.models import Crop


# modelo crop calendar

class CropCalendar(models.Model):
    id = models.BigAutoField(primary_key=True)
    crop_start_date = models.DateField('Inicio del cultivo', auto_now=False, auto_now_add=True, null=True)
    crop_end_date = models.DateField('Cosecha el cultivo', auto_now=False, auto_now_add=False, null=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_crop = models.ForeignKey(Crop, on_delete=models.CASCADE)

    @property
    def calendar(self):
        return f"{self.crop_start_date} + {self.crop_end_date}"

    # def __init__(self, *args, **kwargs):
    #     super().__init__(args, kwargs)
    #     self.Crop = None
    #
    # def save(self, *args, **kwargs):
    #     self.fecha_final_cultivo = self.fecha_inicio_cultivo + timedelta(days=self.Crop.tiempo_cosecha)
    #     super().save(*args, **kwargs)
