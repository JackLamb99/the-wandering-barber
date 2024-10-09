from django import forms
from services.models import Service


class BookingForm(forms.Form):
    appointment_date = forms.DateField(
        input_formats=['%d-%m-%Y'],
        widget=forms.HiddenInput()
    )
    selected_time = forms.ChoiceField(
        choices=[
            ('07:00', '07:00'),
            ('10:00', '10:00'),
            ('13:00', '13:00')
        ],
        widget=forms.RadioSelect(attrs={'class': 'btn btn-primary time-btn'})
    )
    address = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address 1', 'required': 'required'})
    )
    address2 = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address 2 (Optional)'})
    )
    city = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City', 'required': 'required'})
    )
    postcode = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Postcode', 'required': 'required'})
    )
    total_price = forms.DecimalField(widget=forms.HiddenInput(), required=True)
    total_duration = forms.IntegerField(widget=forms.HiddenInput(), required=True)
    selected_services = forms.MultipleChoiceField(
        choices=[(service.id, service.name) for service in Service.objects.all()],
        widget=forms.CheckboxSelectMultiple()
    )
