from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from myapp.models import Room, RoomType, Building, BlockedDay
from datetime import date, timedelta

class AvailableRoomsViewTestCase(APITestCase):
    def setUp(self):
        # Create a building, room type, and room
        self.building = Building.objects.create(name='Building 1')
        self.room_type = RoomType.objects.create(name='Room Type 1', type='Single', building=self.building)
        self.room = Room.objects.create(number=101, room_type=self.room_type, price=100.0)

        # Block some days for the room
        today = date.today()
        blocked_days = [
            today + timedelta(days=1),
            today + timedelta(days=2),
            today + timedelta(days=3),
            today + timedelta(days=4),
        ]
        for day in blocked_days:
            BlockedDay.objects.create(day=day, room=self.room)

    def test_available_rooms(self):
        # Define the URL for the endpoint
        url = reverse('available_rooms')

        # Define the check-in and check-out dates
        check_in = date.today() + timedelta(days=5)
        check_out = date.today() + timedelta(days=10)

        # Make a GET request to the endpoint with the check-in, check-out, and building parameters
        response = self.client.get(url, {'check_in': check_in, 'check_out': check_out, 'building': 'Building 1'})

        # Check that the response has a 200 status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that the response contains the available room
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['number'], self.room.number)
        self.assertEqual(response.data[0]['room_type'], self.room.room_type.name)
        self.assertEqual(response.data[0]['price'], str(self.room.price))

    def test_no_available_rooms(self):
        # Define the URL for the endpoint
        url = reverse('available_rooms')

        # Define the check-in and check-out dates
        check_in = date.today() + timedelta(days=1)
        check_out = date.today() + timedelta(days=4)

        # Make a GET request to the endpoint with the check-in, check-out, and building parameters
        response = self.client.get(url, {'check_in': check_in, 'check_out': check_out, 'building': 'Building 1'})

        # Check that the response has a 200 status code
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that the response does not contain any available rooms
        self.assertEqual(len(response.data), 0)

    def test_invalid_building_name(self):
        # Define the URL for the endpoint
        url = reverse('available_rooms')

        # Define the check-in and check-out dates
        check_in = date.today() + timedelta(days=1)
        check_out = date.today() + timedelta(days=4)

        # Make a GET request to the endpoint with an invalid building name
        response = self.client.get(url, {'check_in': check_in, 'check_out': check_out, 'building': 'Building 2'})

        # Check that the response has a 400 status code
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
