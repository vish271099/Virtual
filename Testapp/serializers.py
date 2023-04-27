from rest_framework import serializers
from .models import *

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('number','room_type','price')
    def to_representation(self,instance):
        data=super(RoomSerializer,self).to_representation(instance)
        data['room_type']=instance.room_type.name
        return data