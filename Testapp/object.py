from .models import *
from datetime import timedelta, date, timezone


# Create Building Object
building = Building.objects.create(name="Building ABC")

# Create Room Type Object
room_type = RoomType.objects.create(name ="Single Room",
                                    type="Single",
                                    building=building)

# Create Room Object
room = Room.objects.create(number = 101, 
                           room_type = room_type,
                           price = 100.00)

# 20 Blocked Days
start_date = date(2022, 12, 1)
end_date = date(2022, 12, 10)
start_date_1 = date(2022, 12, 20)
end_date_1 = date(2022, 12, 30)

blocked_days = []
for i in range((end_date - start_date).days + 1):
    day = start_date + timedelta(days=i)
    blocked_day = BlockedDay.objects.create(day=day, room=room)
    blocked_days.append(blocked_day)

for i in range((end_date_1 - start_date_1).days + 1):
    day = start_date + timedelta(days=i)
    blocked_day = BlockedDay.objects.create(day=day, room=room)
    blocked_days.append(blocked_day)

# Genrate random days for any future dates:
for i in range(10):
    day = timezone.now().date() + timedelta(days= i+1)
    blocked_days = BlockedDay.objects.create(day=day, room=room)
