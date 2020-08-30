from django.db import models
from django.utils import timezone

# Create your models here.
class Records(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True)
    current_balance = models.CharField(max_length=100000000, null=True)
    mobile_number = models.CharField(max_length=10)
    residence = models.CharField(max_length=50, null=True)
    occupation = models.CharField(max_length=150, null=True)
    recorded_at = models.DateTimeField(default=timezone.now, blank=True)
    def __str__(self):
        return self.first_name