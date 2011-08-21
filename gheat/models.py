from django.contrib.auth.models import User
from django.db import models

from gheat import managers

class Point(models.Model):
    """
        A simple representation of a point inside the gheat database
    """
    user = models.ForeignKey(User, null=True)
    uid = models.CharField(max_length=100, name='unique identifier')
    latitude = models.FloatField(name='Latitude', db_column='lat', blank=True)
    longitude = models.FloatField(name='Longitude', db_column='lng', blank=True)
    date_added = models.DateTimeField(null=True)
    modtime = models.DateTimeField(auto_now = True, name='Last modification time', null=True)
    density = models.PositiveIntegerField(default=0, editable=False, name='density of the current point')
    
    objects = managers.PointManager()
    
    class Meta:
      ordering = ('-date_added',)