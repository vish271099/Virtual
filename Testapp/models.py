from django.db import models


class Building(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class RoomType(models.Model):
    TYPE_CHOICES = (
        ('single', 'Single'),
        ('double', 'Double'),
    )
    name = models.CharField(max_length=200)
    type = models.CharField(choices=TYPE_CHOICES, max_length=20, default='single')
    building = models.ForeignKey(Building, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.type})"


class Room(models.Model):
    number = models.PositiveSmallIntegerField()
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    price = models.FloatField()

    def __str__(self):
        return f"Room {self.number} ({self.room_type}) - ${self.price}"

class BlockedDay(models.Model):
    day = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.room} is blocked on {self.day}"
