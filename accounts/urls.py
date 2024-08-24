from django.contrib import admin
from django.urls import path
from accounts.views import *

app_name = "accounts"

urlpatterns = [
    path("", login, name="login"),
    path("signup/", signup, name="signup"),
]
