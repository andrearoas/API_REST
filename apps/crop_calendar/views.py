from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from apps.crop_calendar.models import CropCalendar
from apps.crop_calendar.serializers import CalendarSerializer


# Create your views here.
class CalendarList(generics.ListCreateAPIView):
    queryset = CropCalendar.objects.all()
    serializer_class = CalendarSerializer


class CalendarCreate(generics.CreateAPIView):
    queryset = CropCalendar.objects.all()
    serializer_class = CalendarSerializer
    permission_classes = (IsAuthenticated,)


class CalendarUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = CropCalendar.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = CalendarSerializer
