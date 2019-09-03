from rest_framework.generics import (ListAPIView, RetrieveAPIView, 
	RetrieveUpdateAPIView, DestroyAPIView)
from datetime import datetime

from .models import Flight, Booking
from .serializers import (FlightSerializer,	BookingSerializer,
	BookingDetailSerializer, BookingUpdateSerializer)

################ FLIGHT CLASSES ################

class FlightsList(ListAPIView):
	queryset = Flight.objects.all()
	serializer_class = FlightSerializer

################ BOOKING CLASSES ################

class BookingsList(ListAPIView):
	queryset = Booking.objects.filter(date__gte=datetime.today())
	serializer_class = BookingSerializer

class BookingDetail(RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'booking_id'

class BookingUpdate(RetrieveUpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'booking_id'

class BookingDelete(DestroyAPIView):
    queryset = Booking.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'booking_id'

