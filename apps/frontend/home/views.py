from django.shortcuts import render
from django.views.generic import ListView, CreateView
from apps.backend.booking.models import Booking
from apps.backend.footer.models import Footer
from apps.backend.room.models import Room
from apps.backend.banner.models import Banner
from apps.backend.aboutUs.models import aboutUs
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.http import JsonResponse
from .forms import BookingForm


# Create your views here.
class HomeView(ListView):
    model = Room
    template_name = 'frontend/home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banners'] = Banner.objects.all()
        context['rooms'] = Room.objects.filter(status=True).order_by('position')
        context['footerName'] = Footer.objects.filter(title='name').first()
        context['footerNumber'] = Footer.objects.filter(title='contact').first()
        context['footerEmail'] = Footer.objects.filter(title='email').first()
        context['footerCopyright'] = Footer.objects.filter(title='copyright').first()

        if context['footerName'] is None:
            context['footerName'] = "Hotel Name"
        if context['footerNumber'] is None:
            context['footerNumber'] = "9869286303"
        if context['footerEmail'] is None:
            context['footerEmail'] = "aakkashsubedi@gmail.com"
        if context['footerCopyright'] is None:
            context['footerCopyright'] = "Akash's Hotel"
        return context


# Create your views here.
class aboutUsView(ListView):
    model = aboutUs
    template_name = 'frontend/aboutUs/index.html'


class BookingView(SuccessMessageMixin, CreateView):
    model = Booking
    template_name = "frontend/booking/index.html"
    form_class = BookingForm
    success_message = "Room Successfully Booked."
    success_url = reverse_lazy('booking')


def get_room_names(request):
    room_type_id = request.GET.get('room_type_id')
    if room_type_id:
        room_names = Room.objects.filter(type_id=room_type_id).values_list('id', 'title')
        return JsonResponse({'room_names': list(room_names)})
    return JsonResponse({'room_names': []})


def get_room_prices(request):
    room_name = request.GET.get('room_name')
    if room_name:
        room_names = Room.objects.filter(id=room_name).first()
        return JsonResponse({'room_prices': room_names.price})
    return JsonResponse({'room_prices': None})
