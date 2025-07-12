from django.urls import path

from client.views import UserView
from rest_framework.authtoken.views import obtain_auth_token


app_name = "client"

urlpatterns = [
    path("register/", UserView.as_view()),
    path("login/", obtain_auth_token),
]
