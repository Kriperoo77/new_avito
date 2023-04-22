from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.CharField(
        max_length=12,
        verbose_name='телефон',
        null=True,
        blank=True
    )
    is_active = models.BooleanField(
        verbose_name='Активен',
        default=False
    )
    activation_code = models.CharField(
        max_length=128,
        blank=True,
        null=True,
        verbose_name='Код активации'
    )
    email = models.EmailField('email address', blank=True, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        self.username = self.email
        super().save(*args, **kwargs)

    class Meta:
        verbose_name= 'Пользователь'
        verbose_name_plural = 'Пользователь'
    
    def __str__(self) -> str:
        return self.email
