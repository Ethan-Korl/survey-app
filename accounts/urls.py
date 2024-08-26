from django.contrib import admin
from django.urls import path
from accounts.views import *

app_name = "accounts"

urlpatterns = [
    path("", LoginView.as_view(), name="login"),
    path("signup/", RegisterView.as_view() , name="signup"),
]
