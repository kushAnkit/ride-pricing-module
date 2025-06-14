from django.contrib import admin

# Register your models here.
from .models import (
    PricingConfiguration,
    DistanceBasePrice,
    DistanceAdditionalPrice,
    TimeMultiplier,
    WaitingCharge,
    ConfigChangeLog
)

from .forms import PricingConfigurationForm

# Inlines
class DistanceBasePriceInline(admin.TabularInline):
    model = DistanceBasePrice
    extra = 1

class DistanceAdditionalPriceInline(admin.TabularInline):
    model = DistanceAdditionalPrice
    extra = 1

class TimeMultiplierInline(admin.TabularInline):
    model = TimeMultiplier
    extra = 1

class WaitingChargeInline(admin.TabularInline):
    model = WaitingCharge
    extra = 1

# PricingConfiguration admin
@admin.register(PricingConfiguration)
class PricingConfigurationAdmin(admin.ModelAdmin):
    form = PricingConfigurationForm
    inlines = [
        DistanceBasePriceInline,
        DistanceAdditionalPriceInline,
        TimeMultiplierInline,
        WaitingChargeInline
    ]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        from .models import ConfigChangeLog
        ConfigChangeLog.objects.create(
            config=obj,
            user=request.user,
            action="Updated" if change else "Created"
        )

    def delete_model(self, request, obj):
        from .models import ConfigChangeLog
        ConfigChangeLog.objects.create(
            config=obj,
            user=request.user,
            action="Deleted"
        )
        super().delete_model(request, obj)

admin.site.register(ConfigChangeLog)

