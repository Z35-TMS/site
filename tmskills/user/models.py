from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="Пользовательский Email.")
    phone = models.CharField(max_length=20, verbose_name="Номер пользователя.")
    sex = models.CharField(max_length=1, verbose_name="Пол пользователя.")

    class Meta:
        db_table="tms_user"
        verbose_name="Пользователь"
        verbose_name_plural="Пользователи"