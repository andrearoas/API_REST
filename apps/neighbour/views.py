from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from apps.neighbour.models import Neighbour
from apps.neighbour.serializers import NeighbourSerializer


# Create your views here.
class NeighbourList(generics.ListAPIView):
    queryset = Neighbour.objects.all()
    serializer_class = NeighbourSerializer


class NeighbourCreate(generics.CreateAPIView):
    queryset = Neighbour.objects.all()
    serializer_class = NeighbourSerializer
    permission_classes = (IsAuthenticated,)


class NeighbourUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Neighbour.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = NeighbourSerializer
