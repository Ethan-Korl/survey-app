from main.views import sp_dashboard
from main.views import (
    GetQuetionsForSp,
    CreateFileResponseView,
    CreateImageResponseView,
    CreateTextResponseView,
    CreateSelectionResponseView,
    CreateNumberResponseView,
)
from django.urls import path


urlpatterns = [
    path("sp-response/<url_id>/", sp_dashboard, name="sp-dashboard"),
    path("api/get-questions/<url_id>/", GetQuetionsForSp.as_view(), name="questions"),
    path(
        "api/submit-image-response/",
        CreateImageResponseView.as_view(),
        name="questions",
    ),
    path(
        "api/submit-file-response/", CreateFileResponseView.as_view(), name="questions"
    ),
    path(
        "api/submit-text-response/", CreateTextResponseView.as_view(), name="questions"
    ),
    path(
        "api/submit-selection-response/",
        CreateSelectionResponseView.as_view(),
        name="questions",
    ),
    path(
        "api/submit-number-response/",
        CreateNumberResponseView.as_view(),
        name="questions",
    ),
]
