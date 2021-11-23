from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, IntegerField, TextField
from django.db.models.fields.related import ForeignKey
from chips_project.settings import AUTH_USER_MODEL

class Chips(models.Model):        
    name = CharField(max_length = 64)
    packaging = models.CharField(choices=(("packet","packet"),("container","container")),max_length=255)
    air_percentage = IntegerField()
    description = TextField(default = "")
    user = ForeignKey(AUTH_USER_MODEL, on_delete = CASCADE)

    class Meta:
        verbose_name = "Chips"
        verbose_name_plural = "Chips"

    def __str__(self):
        return self.name