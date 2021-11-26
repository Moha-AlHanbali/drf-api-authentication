from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    gender = models.CharField(choices=(("male","male"),("female","female")),max_length=255)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"