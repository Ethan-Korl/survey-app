import urllib.parse
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from main.models import Survey, Question
from typing import Any
from main.repository import SurveyRepository, QuestionRepository
from main.serializers import CreateSurveySerializer
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status
import matplotlib.pyplot as plt
import io
import numpy as np
import urllib, base64

# Create your views here.


survey_repo = SurveyRepository
que_repo = QuestionRepository


def test(request):

    x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
    y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
    colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

    plt.scatter(x, y, c=colors, cmap="viridis")

    plt.colorbar()
    fig = plt.gcf()
    buf = io.BytesIO()

    fig.savefig(buf, format="png")
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)

    return render(request, "graph.html", {"data": uri})


def sa_dashboard(request: HttpRequest) -> HttpRequest:
    return render(
        request,
        "sa_dashboard.html",
    )


def survey_detail(request, survey_id):
    survey = survey_repo.get_by_id(survey_id)
    return render(request, "survey_detail.html", {"survey": survey})


def create_question(request, survey_id):
    return render(request, "sa_questions.html")


def create_options(request, question_id):
    question = que_repo.get_by_id(question_id=question_id)
    return render(request, "sa_question_options.html", {"question": question})


def survey_questions(request, survey_id):
    return render(request, "survey_questions.html")


def question_results(request, question_id):
    return render(request, "sa_question_responses.html")
