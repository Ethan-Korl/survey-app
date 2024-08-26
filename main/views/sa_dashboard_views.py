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


survey_repo = SurveyRepository


def sa_dashboard(request: HttpRequest) -> HttpRequest:
    return render(
        request,
        "sa_dashboard.html",
    )


def survey_detail(request, survey_id):
    return render(request, "survey_detail.html")


def create_question(request, survey_id):
    return render(request, "sa_questions.html")


def survey_questions(request, survey_id):
    return render(request, "survey_questions.html")


def question_results(request, question_id):
    return render(request, "sa_question_responses.html")
