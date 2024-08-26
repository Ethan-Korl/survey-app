from main.views import (
    sa_dashboard,
    create_survey,
    survey_detail,
    CreateSurveyView,
    ListSurveyView,
    DeleteSurveyView,
    survey_result,
)
from django.urls import path


sa_urlpatterns = [
    path("sa-dashboard/", sa_dashboard, name="sa-dashboard"),
    path("create-survey/", create_survey, name="create-survey"),
    path("survey-result/", survey_result, name="survey-result"),
    path("survey-detail/", survey_detail, name="survey-detail"),
    path("api/create-survey/", CreateSurveyView.as_view(), name="create-survey-api"),
    path("api/get-surveys/", ListSurveyView.as_view(), name="list-survey-api"),
    path(
        "api/delete-survey/<survey_id>/",
        DeleteSurveyView.as_view(),
        name="delete-survey-api",
    ),
]
