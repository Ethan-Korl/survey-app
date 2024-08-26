from main.views import sp_dashboard
from django.urls import path


urlpatterns = [
    path("sp-response/<url_id>/", sp_dashboard, name="sp-dashboard"),
]
