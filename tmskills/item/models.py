from django.db import models


class Item(models.Model):
    COLORS = [
        ("R", "red"),
        ("W", "white"),
        ("B", "black"),
        ("G", "gray"),
    ]

    def load_photo(self, filename):
        file_type = filename.split(".")[-1]
        file_name = ".".join(["{}/{}_{}_{}_{}", file_type])
        return file_name.format(
            self.brend,
            self.model,
            self.body,
            self.color,
            self.year,
        )

    brend = models.CharField(max_length=20, verbose_name="Марка авто.")
    model = models.CharField(max_length=20, verbose_name="Модель авто.")
    body = models.CharField(max_length=20, verbose_name="Кузов авто.")
    year = models.IntegerField(verbose_name="Год выпуска")
    color = models.CharField(max_length=1, verbose_name="Цвет кузова.")
    cost = models.FloatField(verbose_name="Стоимость авто.")
    desc = models.TextField(verbose_name="Описание товара.")
    amount = models.IntegerField(verbose_name="Количество товара.")
    new = models.BooleanField(default=True, verbose_name="Состояние - новый/бу.")
    photo = models.ImageField(upload_to=load_photo, verbose_name="Фотография авто.")

    class Meta:
        db_table = "items"
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
