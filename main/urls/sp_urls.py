from main.views import sp_dashboard
from main.views import GetQuetionsForSp
from django.urls import path


urlpatterns = [
    path("sp-response/<url_id>/", sp_dashboard, name="sp-dashboard"),
    path("api/get-questions/<url_id>/", GetQuetionsForSp.as_view(), name="questions"),
]
