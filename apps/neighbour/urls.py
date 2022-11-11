from apps.neighbour.views import (NeighbourList, NeighbourCreate, NeighbourUpdateDestroy)
from django.urls import path

urlpatterns = [
    path('neighbour_create/', NeighbourCreate.as_view()),
    path('neighbours/', NeighbourList.as_view()),
    path('neighbours/<int:pk>', NeighbourUpdateDestroy.as_view()),
]
