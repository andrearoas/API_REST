from django.urls import path
from apps.category.views import (CategoryCreate, Categories, CategoryList)

urlpatterns = [
    path('category_create/', CategoryCreate.as_view()),
    path('categories/', CategoryList.as_view()),
    path('categories/<int:pk>', Categories.as_view()),
]
