from  main.views import (sa_dashboard, 
                         create_survey, 
                         survey_detail, 
                         CreateSurveyView,
                         survey_result,
                         sp_dashboard,
                         )
from django.urls import path

urlpatterns = [
    path('sa-dashboard/', sa_dashboard, name="sa-dashboard"),
    path('sp-dashboard/<url_id>/', sp_dashboard, name="sp-dashboard"),
    path('create-survey/', create_survey, name="create-survey"),
    path('survey-result/', survey_result, name="survey-result"),
    path('survey-detail/', survey_detail, name="survey-detail"),
    
    
    path('api/create-survey/', CreateSurveyView.as_view(), name="create-survey-api"),
]
