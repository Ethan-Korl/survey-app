from main.views import sp_dashboard
from django.urls import path


sp_urlpatterns = [
    path("sp-reponse/<url_id>/", sp_dashboard, name="sp-dashboard"),
]
