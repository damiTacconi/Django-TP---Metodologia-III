from .views import *
from django.urls import path

urlpatterns = [
    path('', index, name="index"),
    path('ownerships/<int:ownership_id>', ownership_details, name="ownership_details")
]