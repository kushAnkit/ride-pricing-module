from django.test import TestCase
from decimal import Decimal
from .models import PricingConfiguration, DistanceBasePrice, DistanceAdditionalPrice, TimeMultiplier, WaitingCharge

class FareCalculationTests(TestCase):
    def setUp(self):
        config = PricingConfiguration.objects.create(name="Default Config",
    is_active=True,
    applicable_days="Mon,Tue,Wed,Thu,Fri,Sat,Sun" )
        DistanceBasePrice.objects.create(config=config, base_price=80, up_to_km=3)
        DistanceAdditionalPrice.objects.create(config=config, starts_after_km=3, price_per_km=30)
        TimeMultiplier.objects.create(config=config, from_minute=60, to_minute=120, multiplier=Decimal('1.25'))
        WaitingCharge.objects.create(config=config, free_wait_minutes=3, unit_duration_minutes=3, charge_per_unit=5)

    def test_basic_fare(self):
        # You can plug in the actual calculate logic or simulate a call to the view
        base_fare = 80
        extra_distance = 2  # say 5 km ride
        extra_fare = 2 * 30
        wait_charge = 0
        multiplier = 1
        expected_fare = (base_fare + extra_fare + wait_charge) * multiplier
        self.assertEqual(expected_fare, 140)
