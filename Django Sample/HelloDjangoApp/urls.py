from .views import ListMessageView
from django.conf.urls import url

urlpatterns = [
    url('resources/SampleDB.db', ListMessageView.as_view(), name="Sample")
]
