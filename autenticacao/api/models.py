from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    idade = models.IntegerField()
    cadastro = models.DateField(auto_now_add=True)
