from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from accounts.auth_backend import JWTBackend, Authentication
from accounts.models import SurveyAdmin
from accounts.repository import SurveyAdminRepository
from accounts.serializers import SurveyAdminSerializer
from rest_framework.generics import CreateAPIView, GenericAPIView
# from django.
# Create your views here.


sa_repo = SurveyAdminRepository

def signup(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        confirm_password = request.POST.get('confirm_password')
        try:
            if sa_repo.get_by_username(username) is not None:
                context = {"message": "username already"}
                return render(request, "htmx_components/error_message.html", context)
            
            if not (password == confirm_password):
                context = {"message": "password not matching"}
                return render(request, "htmx_components/error_message.html", context)
            
            sa_repo.create(username=username, password=password)
            Authentication.login(request, username, password)
            response = HttpResponse()
            response['HX-Redirect'] = f'/sa/sa-dashboard/'
            return response
        except Exception as ec:
            print(ec)
            context = {"message": "Error occured"}
            return render(request, "htmx_components/error_message.html", context)
        
    return render(request, "sa_register.html")



def login(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        JWTBackend()
    return render(request, "sa_login.html")




    



