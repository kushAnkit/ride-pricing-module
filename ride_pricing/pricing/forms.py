from django import forms
from .models import PricingConfiguration
import json

VALID_DAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

class PricingConfigurationForm(forms.ModelForm):
    class Meta:
        model = PricingConfiguration
        fields = '__all__'

        
    def clean_applicable_days(self):
        data = self.cleaned_data['applicable_days']
        if isinstance(data, str):
            try:
                data = json.loads(data)
            except json.JSONDecodeError:
                raise forms.ValidationError("Enter valid JSON list (e.g., [\"Mon\", \"Tue\"])")

        if not isinstance(data, list) or not all(day in VALID_DAYS for day in data):
            raise forms.ValidationError(f"Days must be a list containing only: {', '.join(VALID_DAYS)}")

        return data