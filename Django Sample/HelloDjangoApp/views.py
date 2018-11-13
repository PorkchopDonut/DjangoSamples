from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from .models import Message
import sqlite3
import os

def index(request):
    return render(
        request,
        "HelloDjangoApp/index.html",
        {
            'title': "All Messages",
            'greeting': "All Messages",
            'messages': Message.objects.order_by('-date').only('number', 'sender', 'message', 'date', 'read')
        }
    )

def unread(request):
    return render(
        request,
        "HelloDjangoApp/index.html",
        {
            'title' : "Unread Messages",
            'greeting' : "Unread Messages",
            'messages' : Message.objects.filter(read=False).order_by('-date').only('number', 'sender', 'message', 'date', 'read')
        }
    )