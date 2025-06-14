from decimal import Decimal
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import HttpResponse
from django.utils import timezone
from .forms import PricingConfigurationForm
from .models import (
    PricingConfiguration,
    DistanceBasePrice,
    DistanceAdditionalPrice,
    TimeMultiplier,
    WaitingCharge,
    ConfigChangeLog
)

def calculate_fare(request):
    try:
        distance_km = Decimal(request.GET.get('distance', '0'))
        time_minutes = int(request.GET.get('time', '0'))
        wait_minutes = int(request.GET.get('wait', '0'))
    except Exception:
        return JsonResponse({"error": "Invalid input. Please provide numeric values."}, status=400)

    config = PricingConfiguration.objects.filter(is_active=True).first()
    if not config:
        return JsonResponse({'error': 'No active pricing configuration found'}, status=404)

    # Base fare
    base_price_obj = DistanceBasePrice.objects.filter(config=config).first()
    base_fare = base_price_obj.base_price  # Decimal
    up_to_km = Decimal(str(base_price_obj.up_to_km))

    # Additional fare
    additional_fare_obj = DistanceAdditionalPrice.objects.filter(config=config).first()
    extra_distance = max(Decimal('0'), distance_km - Decimal(str(additional_fare_obj.starts_after_km)))
    extra_fare = extra_distance * additional_fare_obj.price_per_km

    # Time multiplier
    applicable_multiplier = TimeMultiplier.objects.filter(
        config=config,
        from_minute__lte=time_minutes,
        to_minute__gte=time_minutes
    ).first()
    multiplier = Decimal(str(applicable_multiplier.multiplier)) if applicable_multiplier else Decimal('1')

    # Waiting charge
    wait_obj = WaitingCharge.objects.filter(config=config).first()
    wait_minutes_over = max(0, wait_minutes - wait_obj.free_wait_minutes)
    wait_units = wait_minutes_over // wait_obj.unit_duration_minutes
    wait_charge = Decimal(wait_units) * wait_obj.charge_per_unit

    # Total fare
    total_fare = (base_fare + extra_fare + wait_charge) * multiplier

    return HttpResponse(f"Total fare is: {round(float(total_fare), 2)}")

def config_form_view(request):
    if request.method == 'POST':
        form = PricingConfigurationForm(request.POST)
        if form.is_valid():
            config = form.save()

            # Log the creation action
            ConfigChangeLog.objects.create(
                config=config,
                user=request.user if request.user.is_authenticated else None,
                action="Created configuration",
                timestamp=timezone.now()
            )

            return HttpResponse("Configuration saved and change logged successfully.")
    else:
        form = PricingConfigurationForm()
    return render(request, 'pricing/config_form.html', {'form': form})
