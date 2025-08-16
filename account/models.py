from django.contrib.auth.models import AbstractUser
from django.db import models
from main.constant_for_app import ukrainian_name_validator, phone_validator


class UserProfile(AbstractUser):
    first_name = models.CharField(
        max_length=256,
        blank=True,
        validators=[ukrainian_name_validator],
    )

    last_name = models.CharField(
        max_length=256,
        blank=True,
        validators=[ukrainian_name_validator],
    )


    middle_name = models.CharField(
        "По-батькові",
        max_length=15,
        blank=False,
        validators=[ukrainian_name_validator],
    )

    position = models.CharField("Посада", max_length=30)
    cars = models.ManyToManyField("auto.Auto", blank=True)
    email = models.EmailField(blank=True)

    image = models.ImageField(
        upload_to='images/',
        blank=True,
        null=True,
    )

    phone = models.CharField(
        "Телефон",
        max_length=15,
        validators=[phone_validator],
    )






    def __str__(self):
        return self.username


