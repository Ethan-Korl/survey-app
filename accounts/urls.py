from django.contrib import admin
from django.urls import path
from accounts.views import *

urlpatterns = [
    path("", login, name="login"),
    path("signup/", signup, name="signup"),
]
