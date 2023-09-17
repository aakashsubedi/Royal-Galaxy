from django.forms import ModelForm
from django import forms
from apps.backend.booking.models import Booking
from apps.backend.room.models import RoomType


class BookingForm(ModelForm):
    type = forms.ModelChoiceField(queryset=RoomType.objects.all(),
                                      widget=forms.Select(attrs={'class': 'frm-field required', 'id':'country1'}),
                                      empty_label="Select Room Type")
    class Meta:
        model = Booking
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone',
            'booking_date',
            'arrival_date',
            'no_of_people',
            'type',
            'room',
        ]
