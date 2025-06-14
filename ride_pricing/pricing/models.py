from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Choices for Days of the Week
DAYS_OF_WEEK = [
    ('Mon', 'Monday'),
    ('Tue', 'Tuesday'),
    ('Wed', 'Wednesday'),
    ('Thu', 'Thursday'),
    ('Fri', 'Friday'),
    ('Sat', 'Saturday'),
    ('Sun', 'Sunday'),
]

class PricingConfiguration(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    applicable_days = models.JSONField(help_text="List of days (e.g., ['Mon', 'Tue'])")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({'Active' if self.is_active else 'Inactive'})"


class DistanceBasePrice(models.Model):
    config = models.ForeignKey(PricingConfiguration, related_name="distance_base_prices", on_delete=models.CASCADE)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    up_to_km = models.FloatField()

    def __str__(self):
        return f"{self.base_price} INR up to {self.up_to_km} KM"


class DistanceAdditionalPrice(models.Model):
    config = models.ForeignKey(PricingConfiguration, related_name="distance_additional_prices", on_delete=models.CASCADE)
    price_per_km = models.DecimalField(max_digits=10, decimal_places=2)
    starts_after_km = models.FloatField()

    def __str__(self):
        return f"{self.price_per_km} INR/km after {self.starts_after_km} KM"


class TimeMultiplier(models.Model):
    config = models.ForeignKey(PricingConfiguration, related_name="time_multipliers", on_delete=models.CASCADE)
    from_minute = models.PositiveIntegerField(help_text="Start time in minutes (e.g., 60 for 1 hour)")
    to_minute = models.PositiveIntegerField(help_text="End time in minutes (e.g., 120 for 2 hours)")
    multiplier = models.FloatField()

    def __str__(self):
        return f"{self.multiplier}x from {self.from_minute} to {self.to_minute} mins"


class WaitingCharge(models.Model):
    config = models.ForeignKey(PricingConfiguration, related_name="waiting_charges", on_delete=models.CASCADE)
    free_wait_minutes = models.PositiveIntegerField(default=3)
    charge_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    unit_duration_minutes = models.PositiveIntegerField(default=3)

    def __str__(self):
        return f"{self.charge_per_unit} INR per {self.unit_duration_minutes} min after {self.free_wait_minutes} min"


class ConfigChangeLog(models.Model):
    config = models.ForeignKey(PricingConfiguration, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=100)  # e.g., "Activated", "Updated Base Price"
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.action} by {self.user} on {self.timestamp.strftime('%Y-%m-%d %H:%M')}"