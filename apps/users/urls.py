from django.urls import path
from apps.users.views import (Account, UserList, Login, Logout, Signup)

urlpatterns = [
     path('login/', Login.as_view()),
     path('logout/', Logout.as_view()),
     path('signup/', Signup.as_view()),
     path('account/<int:pk>', Account.as_view()),
     path('users/', UserList.as_view()),
]
