from django import forms

from dashboard.models import Farmer


class FarmerForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = "__all__"
