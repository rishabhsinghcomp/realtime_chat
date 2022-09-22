from django.db import models
from datetime import datetime
# Create your models here.


class rooms(models.Model):
    room_name=models.CharField(max_length=100000)


class room_messages(models.Model):
    username=models.CharField(max_length=10000)
    value=models.CharField(max_length=10000)
    room_id=models.CharField(max_length=1000)
    created_at=models.DateTimeField(default=datetime.now,blank=True)
