from django.urls import path
from .views import*

urlpatterns = [
    path('available-rooms/', AvailableRoomsView.as_view(), name='available_rooms')
]
