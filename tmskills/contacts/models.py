from django.db import models

# Create your models here.
class FeedBack(models.Model):
    fullname = models.CharField(max_length=100, verbose_name="Имя просящего.")
    email = models.EmailField(verbose_name="Email просящего.")
    phone = models.CharField(max_length=20, verbose_name="Телефон.")
    message = models.TextField(verbose_name="Сообщение.")
    is_worked = models.BooleanField(default=False, verbose_name="Если обработано.")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Время создания.")

    class Meta:
        db_table = "feedback"
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратная связь."