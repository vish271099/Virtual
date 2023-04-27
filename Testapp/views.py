from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.utils import timezone
from datetime import datetime, timedelta
from rest_framework.views import APIView


# class AvailableRoomsView(generics.ListAPIView):
#     serializers_class = RoomSerializer(many=True)

#     def queryset(self):
#         # Get the dates from the query string 
#         check_in_str = self.request.query_params.get('check_in')
#         check_out_str = self.request.query_params.get('check_out')

#         # Convert dates to objects
#         check_in = datetime.strptime(check_in_str, '%Y-%m-%d').date()
#         check_out = datetime.strptime(check_out_str, '%Y-%m-%d').date()

#         # Get the building name 
#         building_name = self.request.query_params.get('building')

#         # Get the building object
#         try:
#             building = Building.objects.filter(name = building_name)
#         except:
#             return "N/A"
        
#         # Get the blocked days in the given range
#         blocked_days = BlockedDay.objects.filter(day__range=(check_in, check_out))

#         # Get the rooms for the given building
#         available_rooms = Room.objects.filter(room_type__building=building).exclude(blockedday__in=blocked_days)

#         # Sort the available room
#         available_rooms = available_rooms.order_by('price')
#         return available_rooms
    
class AvailableRoomsView(APIView):
    api_view = ['GET']
    serializer_class = RoomSerializer

    def get(self, request):
        check_in_str = request.query_params.get('check_in')
        print(check_in_str)
        check_out_str = request.query_params.get('check_out')
        print(check_out_str)
        building_name = request.query_params.get('building')
        print(building_name)


        # Convert dates to objects
        check_in = datetime.strptime(check_in_str, '%Y-%m-%d').date()
        print(check_in)
        check_out = datetime.strptime(check_out_str, '%Y-%m-%d').date()
        print(check_out)

        # Get the building object
        try:
            building = Building.objects.filter(name = building_name).last()
            print(building)
        except:
            return "N/A"
        # Get the blocked days in the given range
        blocked_days = BlockedDay.objects.filter(day__range=(check_in, check_out)).last()
        print(blocked_days.room.number)

        # Get the rooms for the given building
        # for i in blocked_days:
        available_rooms = Room.objects.filter(room_type__building=building).exclude(number=blocked_days.room.number).order_by('price')
        serializers=self.serializer_class(available_rooms,many=True)
        print(available_rooms)
        return Response(serializers.data, status=status.HTTP_200_OK)