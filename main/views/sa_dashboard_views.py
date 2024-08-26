from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from main.models import Survey, Question
from typing import Any
from main.repository import SurveyRepository
from main.serializers import CreateSurveySerializer
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


survey_repo =  SurveyRepository

def sa_dashboard(request: HttpRequest) -> HttpRequest:
    return render(request, "sa_dashboard.html",)

    
def create_survey(request : HttpRequest):
    return render(request, "htmx_components/create_survey_component.html")


def survey_result(request):
    if request.method == "POST":
        # JWTBackend()
        pass
    return render(request, "survey_result.html")

def survey_detail(request):
    if request.method == "POST":
        # JWTBackend()
        pass
    return render(request, "survey_detail.html")