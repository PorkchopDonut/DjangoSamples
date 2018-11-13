from HelloDjangoApp.models import Message
from .serializers import MessageSerializer, UpdateMessageSerializer
from rest_framework import generics

class ListAPIView(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class UpdateAPIView(generics.UpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = UpdateMessageSerializer