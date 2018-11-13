from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from .models import Message
import sqlite3
import os

def index(request):
    now = datetime.now()

    messages = Message.objects.order_by('-date').only('number', 'sender', 'message', 'date', 'read')

    return render(
        request,
        "HelloDjangoApp/index.html",
        {
            'title': "Hello Django!",
            'greeting': "Hello Django!",
            'content': " on " + now.strftime("%A, %d %B, %Y at %X"),
            'messages': messages
        }
    )

def about(request):
    return render(
        request,
        "HelloDjangoApp/about.html",
        {
            'title' : "About HelloDjangoApp",
            'content' : "Example app page for Django."
        }
    )