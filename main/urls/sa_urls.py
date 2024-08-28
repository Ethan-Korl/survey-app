from main.views import (
    sa_dashboard,
    survey_detail,
    CreateSurveyView,
    CreateQuestionView,
    CreateOptionsView,
    ListQuestionView,
    ListOptionView,
    ListSurveyView,
    DeleteSurveyView,
    survey_questions,
    create_question,
    create_options,
    question_results,
)
from django.urls import path


sa_urlpatterns = [
    path("sa-dashboard/", sa_dashboard, name="sa-dashboard"),
    path("survey-result/<survey_id>/", survey_questions, name="survey-result"),
    path("survey-detail/<survey_id>/", survey_detail, name="survey-detail"),
    path("create-question/<survey_id>/", create_question, name="create-question"),
    path("create-options/<question_id>/", create_options, name="create-option"),
    path(
        "question-responses/<question_id>/", question_results, name="question-results"
    ),
    path("api/create-survey/", CreateSurveyView.as_view(), name="create-survey-api"),
    path("api/get-surveys/", ListSurveyView.as_view(), name="list-survey-api"),
    path(
        "api/get-questions/<survey_id>/",
        ListQuestionView.as_view(),
        name="list-question-api",
    ),
    path(
        "api/get-options/<question_id>/",
        ListOptionView.as_view(),
        name="list-options-api",
    ),
    path(
        "api/create-question-option/",
        CreateOptionsView.as_view(),
        name="create-question-option",
    ),
    path(
        "api/create-question/", CreateQuestionView.as_view(), name="create-question-api"
    ),
    path(
        "api/delete-survey/<survey_id>/",
        DeleteSurveyView.as_view(),
        name="delete-survey-api",
    ),
]
