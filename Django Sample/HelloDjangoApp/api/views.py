from HelloDjangoApp.models import Message
from .serializers import MessageSerializer, UpdateMessageSerializer
from django.db.models import Q
from rest_framework import generics

class ListAPIView(generics.ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        queryset = Message.objects.all()

        read = self.request.query_params.get('read', None)
        if read is not None:
            queryset = queryset.filter(read=read)

        search = self.request.query_params.get('search', None)
        if search is not None:
            queryset = queryset.filter(Q(sender__icontains=search) | Q(message__icontains=search) | Q(date__icontains=search))
        
        return queryset

class UpdateAPIView(generics.UpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = UpdateMessageSerializer