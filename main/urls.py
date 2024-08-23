from  main.views import sa_dashboard
from django.urls import path

urlpatterns = [
    path('sa-dashbaord/', sa_dashboard, name="sa_dashboard"),
]
