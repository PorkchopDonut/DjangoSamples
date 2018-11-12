from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
import sqlite3
import os

def index(request):
    now = datetime.now()
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    conn = sqlite3.connect(os.path.join(__location__, 'resources/SampleDB.db'))
    cursor = conn.cursor()
    messages = []

    for row in cursor.execute("SELECT Message from Sample"):
        messages.append(row[0])

    return render(
        request,
        "HelloDjangoApp/index.html",
        {
            'title': "Hello Django!",
            'message': "Hello Django!",
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