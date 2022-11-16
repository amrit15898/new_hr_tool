from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
domain = (("Python Develper", "Python Developer"),
          ("Php Developer", "Php Developer"))
role = (
    ("Admin", "Admin"),
    ("HR", "HR"), 
    ("MD", "MD"),
    ("TLeader", "TLeader"),
    ("Employee", "Employee"),
    ("Intern", "Intern")

)

positions = (
    ("Seniour", "Seniour"),
    ("Junior", "Junior"),
    ("Intern", "Intern")

)

class User(AbstractUser):
    domain = models.CharField(max_length=200, choices = domain,null=True)
    role = models.CharField(max_length=20, choices = role)
    position = models.CharField(max_length=20, choices=positions)

    phone = models.CharField(max_length = 200)
    address = models.CharField(max_length = 200)
    is_delete = models.BooleanField(default=False)
    

  


