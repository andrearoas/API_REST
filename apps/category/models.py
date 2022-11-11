from django.db import models


class Category(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name_category = models.CharField(max_length=20)
    type_category = models.SmallIntegerField()

    @property
    def __str__(self):
        return f"{self.name_category}"
