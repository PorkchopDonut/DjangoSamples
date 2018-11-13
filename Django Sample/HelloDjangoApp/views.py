from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render, redirect
from .models import Message
import sqlite3
import os

def index(request):
    return render(
        request,
        "HelloDjangoApp/index.html",
        {
            'title' : "All Messages",
            'greeting' : "All Messages",
            'page' : "read",
            'messages' : Message.objects.order_by('-date').only('number', 'sender', 'message', 'date', 'read')
        }
    )

def unread(request):
    return render(
        request,
        "HelloDjangoApp/index.html",
        {
            'title' : "Unread Messages",
            'greeting' : "Unread Messages",
            'page' : 'unread',
            'messages' : Message.objects.filter(read=False).order_by('-date').only('number', 'sender', 'message', 'date', 'read')
        }
    )

def update(request):
    Message.objects.filter(number=request.GET.get('number')).update(read=request.GET.get('mark'))

    return redirect(request.GET.get('next', 'index'))

def search(request):
    Message.objects.filter(number=request.GET.get('number')).update(read=request.GET.get('mark'))

    return redirect(request.GET.get('next', 'index'))