from rest_framework import viewsets, permissions
# from rest_framework.permissions import IsAuthenticated, AllowAny
from apps.crop.models import Crop
from apps.crop.serializers import CropSerializer


class CropViewSet(viewsets.ModelViewSet):
    queryset = Crop.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CropSerializer

# class CropCreate(generics.CreateAPIView):
#     queryset = Crop.objects.all()
#     serializer_class = CropSerializer
#     permission_classes = (AllowAny,)
#
#
# class CropList(generics.ListAPIView):
#     queryset = Crop.objects.all()
#     serializer_class = CropSerializer
#
#
# class CropDestroyUpdate(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Crop.objects.all()
#     permission_classes = (IsAuthenticated,)
#     serializer_class = CropSerializer
