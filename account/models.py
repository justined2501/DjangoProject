from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):
    middel_name = models.CharField("По-батькові", max_length=15)
    position = models.CharField("Посада", max_length=30)
    phone = models.CharField("Телефон", max_length=15)
    cars = models.ManyToManyField("Auto", blank=True)

    def __str__(self):
        return self.username
