from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):
    patronymic = models.CharField("По-батькові", max_length=15)
    post = models.CharField("Посада", max_length=30)
    number = models.CharField("Телефон", max_length=15)
    count_of_sold_cars = models.IntegerField("Продано машин", default=0)
    sold_car = models.ManyToManyField("Auto", blank=True)



    def __str__(self):
        return self.username


class Auto(models.Model):
    title = models.CharField("Назва виробника", max_length=15)
    year_of_release = models.IntegerField("Рiк випуску")
    model = models.CharField("Модель", max_length=15)
    Cost = models.DecimalField("Собівартість", max_digits=10, decimal_places=2)
    selling_price = models.DecimalField("Потенційна ціна продажу", max_digits=10, decimal_places=2)
    is_sell = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Sales(models.Model):
    worker = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="Співробітник")
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE, verbose_name="Автомобіль")
    date = models.DateField("Дата продажи")
    really_cost = models.IntegerField("Реальная цена продажи")

    def __str__(self):
        return str(self.worker)
