from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from auth_backend.backends import JWTBackend
# from django.
# Create your views here.



def signup():
    pass



def login(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        JWTBackend()
    return render(request, "sa_login.html")




