from uuid import uuid4

from django.db import models


class Sale(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    buyer = models.TextField()
    description = models.TextField()
    unit_price = models.FloatField()
    quantity = models.PositiveIntegerField()
    address = models.TextField()
    provider = models.TextField()
