from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.CharField(max_length=20, unique=True)
    role = models.CharField(max_length=50, choices=[
        ('zakroyschik', 'Закройщик'),
        ('four_x', '4-х'),
        ('raspash', 'Распаш'),
        ('beika', 'Бейка'),
        ('strochka', 'Строчка'),
        ('gorlo', 'Горло'),
        ('ytyg', 'Утюг'),
        ('otk', 'ОТК'),
        ('ypakovka', 'Упаковка'),
    ])

    def __str__(self):
        return f"{self.last_name} {self.first_name} - {self.number}"
