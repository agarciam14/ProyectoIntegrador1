from django.db import models
import uuid

class Ultrasonic(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    distance = models.IntegerField(verbose_name='distance')
    lat = models.DecimalField(verbose_name='lat',max_digits=10, decimal_places=5)
    lng = models.DecimalField(verbose_name='lng',max_digits=10, decimal_places=5)
    area = models.DecimalField(verbose_name='area',max_digits=10, decimal_places=5)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)