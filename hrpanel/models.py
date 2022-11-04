

from email.policy import default
from django.db import models
from adminpanel.models import *


# Create your models here.
class Interview(models.Model):
    name = models.CharField(max_length = 200)
    domain = models.ForeignKey(Domain, on_delete = models.PROTECT)
   
   
    datetime = models.DateTimeField(auto_now_add=False, auto_now=False)
    interviewers = models.ManyToManyField(User)
    is_delete = models.BooleanField(default=False)
    # cv = models.ImageField(upload_to = "static/images", null=Trure, blank= Tur)

    


class Meeting(models.Model):
    agenda = models.CharField(max_length =200)
    description = models.TextField()
    with_us = models.ManyToManyField(User)
    date_time = models.DateTimeField(auto_now_add=False, auto_now = False)
    

    