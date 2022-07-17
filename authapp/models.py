from django.contrib.auth.models import AbstractUser
from django.db import models

from mainapp.models import NULLABLE


class User(AbstractUser):
    email = models.EmailField(blank=True, unique=True, verbose_name='Email')
    age = models.PositiveSmallIntegerField(**NULLABLE, verbose_name='Возраст')
    avatar = models.ImageField(upload_to='users', **NULLABLE)

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
