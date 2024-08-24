from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from main.models import Survey, Question
from typing import Any
from main.repository import SurveyRepository
# Create your views here.


survey_repo =  SurveyRepository

def sa_dashboard(request: HttpRequest) -> HttpRequest:
    context: dict[str, Any] = {}
    return render(request, "sa_dashboard.html", context)


def create_survey(request : HttpRequest):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        
        survey = survey_repo.create(title=title,
                           description=description
                           )
        survey.generate_url()
        
        response = HttpResponse()
        response['HX-Redirect'] = f'/sa/sa-dashboard/'
        return response
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