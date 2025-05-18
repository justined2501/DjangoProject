from django.db import models


class Auto(models.Model):
    brand = models.CharField("Назва виробника", max_length=15)
    year_of_release = models.IntegerField("Рiк випуску")
    model = models.CharField("Модель", max_length=15)
    cost = models.DecimalField("Собівартість", max_digits=10, decimal_places=2)
    selling_price = models.DecimalField("Потенційна ціна продажу", max_digits=10, decimal_places=2)
    is_sell = models.BooleanField(default=False)
    created_at = models.DateField(verbose_name="Дата створення", auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.brand

class Brand(models.Model):
    name = models.CharField("Назва виробника", max_length=15)

