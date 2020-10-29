from django.db import models
from user.models import User
from item.models import Item


class Bucket(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bucket")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="bucket")
    status = models.BooleanField(
        default=False, verbose_name="Статус заказа: (оформляется/нет)"
    )
    add_time = models.DateTimeField(
        auto_now_add=True, verbose_name="Всеря добавления в карзину."
    )
    change_status = models.DateTimeField(
        auto_now=True, verbose_name="Время изменения статуса."
    )

    class Meta:
        db_table = "bucket"
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"