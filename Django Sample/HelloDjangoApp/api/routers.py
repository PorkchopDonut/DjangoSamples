from .views import ListAPIView, UpdateAPIView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'messages', ListAPIView)
router.register(r'messages/update', UpdateAPIView)