from apps.crop_calendar.views import (CalendarUpdateDestroy, CalendarList, CalendarCreate)
from django.urls import path

urlpatterns = [
    path('calendar_create/', CalendarCreate.as_view()),
    path('calendars/', CalendarList.as_view()),
    path('calendar/<int:pk>', CalendarUpdateDestroy.as_view()),
]
