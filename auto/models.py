from django.db import models


class Auto(models.Model):
    title = models.CharField("Назва виробника", max_length=15)
    year_of_release = models.IntegerField("Рiк випуску")
    model = models.CharField("Модель", max_length=15)
    cost = models.DecimalField("Собівартість", max_digits=10, decimal_places=2)
    selling_price = models.DecimalField("Потенційна ціна продажу", max_digits=10, decimal_places=2)
    is_sell = models.BooleanField(default=False)

    def __str__(self):
        return self.title
