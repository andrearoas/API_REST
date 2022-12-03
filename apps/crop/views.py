from rest_framework import generics
from rest_framework.permissions import AllowAny
from apps.crop.models import Crop
from apps.crop.serializers import CropSerializer


class CropCreate(generics.ListCreateAPIView):
    queryset = Crop.objects.all()
    serializer_class = CropSerializer
    permission_classes = [AllowAny]


class CropList(generics.ListAPIView):
    queryset = Crop.objects.all()
    serializer_class = CropSerializer

# class CropDestroyUpdate(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Crop.objects.all()
#     permission_classes = (IsAuthenticated,)
#     serializer_class = CropSerializer
