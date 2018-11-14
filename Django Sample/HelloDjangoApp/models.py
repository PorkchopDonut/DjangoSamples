from django.db import models
from datetime import datetime

class Message(models.Model):
    number = models.IntegerField()
    sender = models.TextField()
    message = models.TextField()
    date = models.TextField(default=datetime.now().strftime('%b %d, %Y at %I:%M %p'))
    read = models.BooleanField()