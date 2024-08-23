from django.http import HttpRequest
from .backends import JWTBackend
from accounts.models import SurveyAdmin
from django.contrib.auth.hashers import make_password, check_password


class Authentication:
    jwt_backend = JWTBackend
    
    @classmethod
    def login(cls, request :HttpRequest, username, password):
        try:
            survey_admin = SurveyAdmin.objects.get(username=username)
            if check_password(survey_admin.password):
                auth_session = JWTBackend.generate_jwt(survey_admin)
                request.COOKIES["auth_session"] = auth_session
                pass
                # response.set_cookie('jwt', token, httponly=True, secure=True)
        except SurveyAdmin.DoesNotExist:
            return None

        token = cls.jwt_backend.generate_jwt(survey_admin)
    
    
    def logout(cls, request: HttpRequest):
        if request.COOKIES["auth_session"]:
            request.COOKIES["auth_session"] = None