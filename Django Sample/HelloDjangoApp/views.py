from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from .models import Message
import sqlite3
import os

def index(request):
    now = datetime.now()
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    conn = sqlite3.connect(os.path.join(__location__, 'resources/SampleDB.db'))
    cursor = conn.cursor()
    messages = []

    for row in cursor.execute("SELECT Number, Sender, Message, Date, Read FROM Sample"):
        messages.append(Message(row[0], row[1], row[2], row[3], row[4]))

    return render(
        request,
        "HelloDjangoApp/index.html",
        {
            'title': "Hello Django!",
            'greeting': "Hello Django!",
            'content': " on " + now.strftime("%A, %d %B, %Y at %X"),
            'messages': displayMessages(messages)
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

def displayMessages(messages):
    output = ""
    
    for message in messages:
        output += "<span class=\"message\">{}</span><br>".format(message.__str__())

    return output