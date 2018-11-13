from django.db import models
from datetime import datetime

class Message(models.Model):
    number = models.IntegerField()
    sender = models.TextField()
    message = models.TextField()
    date = models.DateField(auto_now_add=True)
    read = models.BooleanField()