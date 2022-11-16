

from email.policy import default
from django.db import models
from adminpanel.models import *
from adminpanel.models import domain


result = (("pending", "pending"), ("selected", "selected"), ("rejetected", "rejected"))

# Create your models here.
interview_mode = (("online", "online"), ("offline", "offline"))
class Interview(models.Model):
    name = models.CharField(max_length = 200)
    domain = models.CharField(max_length =200, choices = domain, null=True)
   
   
    datetime = models.DateTimeField(auto_now_add=False, auto_now=False)
    model = models.CharField(max_length=20, choices=interview_mode)
    interviewer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    is_delete = models.BooleanField(default=False)
    attempt = models.IntegerField(null=True, blank=True)
    email= models.EmailField(max_length=200)
    interview_mode = models.CharField(max_length=200, choices=interview_mode, null=True, blank=True)
    cv = models.ImageField(upload_to="static/images", null=True, blank=True)
    result = models.CharField(max_length=20, choices=result, default="pending")
    

    




    # cv = models.ImageField(upload_to = "static/images", null=Trure, blank= Tur)

    


class Meeting(models.Model):
    agenda = models.CharField(max_length =200)
    description = models.TextField()
    with_us = models.ManyToManyField(User)
    date_time = models.DateTimeField(auto_now_add=False, auto_now = False)
    

    