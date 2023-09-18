from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about-us', aboutUsView.as_view(), name='aboutUs'),
    path('feedback', FeedbackView.as_view(), name='feedback'),
    path('booking', BookingView.as_view(), name='booking'),
    path('get_room_names/', get_room_names, name='get_room_names'),
    path('get_room_prices/', get_room_prices, name='get_room_prices'),
]


