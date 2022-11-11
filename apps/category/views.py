from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from apps.category.models import Category
from apps.category.serializers import CategorySerializer


class CategoryCreate(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class Categories(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = CategorySerializer
