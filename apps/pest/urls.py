from apps.pest.views import (PestList, PestCreate, PestUpdateDestroy)
from django.urls import path

urlpatterns = [
    path('pest_create/', PestCreate.as_view()),
    path('pests/', PestList.as_view()),
    path('pests/<int:pk>', PestUpdateDestroy.as_view()),
]
