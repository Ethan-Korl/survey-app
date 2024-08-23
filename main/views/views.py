from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from main.models import Survey, Question
from typing import Any
# Create your views here.



def sa_dashboard(request: HttpRequest) -> HttpRequest:
    context: dict[str, Any] = {}
    return render(request, "sa_dashboard.html", context)
    