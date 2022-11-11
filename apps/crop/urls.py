from django.urls import path
from rest_framework import routers
# from apps.crop.views import (CropCreate, CropList, CropDestroyUpdate)
from apps.crop.views import CropViewSet

router = routers.DefaultRouter()
router.register('api/crop', CropViewSet, 'cropviu')

urlpatterns = router.urls

# urlpatterns = [
#     path('crop_create/', CropCreate.as_view()),
#     path('crops/', CropList.as_view()),
#     path('crops/<int:pk>', CropDestroyUpdate.as_view()),
# ]
