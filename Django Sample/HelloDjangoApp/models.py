from django.db import models

class Message(models.Model):
    number = models.IntegerField()
    sender = models.TextField()
    message = models.TextField()
    date = models.DateField()
    read = models.BooleanField()

    def __init__(self, number, sender, message, date, read):
        self.number = number
        self.sender = sender
        self.message = message
        self.date = date
        self.read = read

    def __str__(self):
        return "{} ({}) - {}".format(self.sender, self.date, self.message)