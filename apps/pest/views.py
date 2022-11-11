from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from apps.pest.serializers import PestSerializer
from apps.pest.models import Pest


# Create your views here.
class PestList(generics.ListAPIView):
    queryset = Pest.objects.all()
    serializer_class = PestSerializer


class PestCreate(generics.CreateAPIView):
    queryset = Pest.objects.all()
    serializer_class = PestSerializer
    permission_classes = (IsAuthenticated,)


class PestUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pest.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = PestSerializer
