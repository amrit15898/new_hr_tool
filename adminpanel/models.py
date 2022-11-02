from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Domain(models.Model):
    name = models.CharField(max_length = 200)


    def __str__(self) -> str:
        return self.name

class Position(models.Model):
    name = models.CharField(max_length = 200)


    def __str__(self) -> str:
        return self.name


class User(AbstractUser):
    domain = models.ForeignKey(Domain, on_delete = models.CASCADE, null=True)
    position = models.ForeignKey(Position, on_delete = models.CASCADE, null=True)
    phone = models.CharField(max_length = 200)
    address = models.CharField(max_length = 200)
    is_delete = models.BooleanField(default=False)

  


