import jwt
from accounts.models import SurveyAdmin
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime, timedelta
from django.contrib.auth.base_user import AbstractBaseUser
from django.conf import settings
from django.http import HttpRequest
from accounts.models import SurveyAdmin
from django.contrib.auth import login
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.base_user import BaseUserManager
from accounts.repository import SurveyAdminRepository
from django.contrib.auth.hashers import make_password, check_password


sa_repo = SurveyAdminRepository

# class BaseSurveyAdminManager:
    
#     @staticmethod
#     def create_survey_admin(username, password):
    

sa_repo = SurveyAdminRepository

class BaseSurveyAdminManager(BaseUserManager):
    @staticmethod
    def create_survey_admin(username, password, **extra_fields):
        _harshed_password = make_password(password)
        print(_harshed_password)
        survey_admin = sa_repo.create(
                                username=username, 
                                password=_harshed_password,
                            )
        return survey_admin
    
       
class SimpleJWTBackend(BaseBackend):
    
    @staticmethod
    def authenticate(username=None, password=None, **kwargs):
        try:
            survey_admin = sa_repo.get_by_username(username=username)
            if survey_admin is None:
                raise SurveyAdmin.DoesNotExist
                
            if check_password(password, survey_admin.password):
                return survey_admin
            
            return None
        except SurveyAdmin.DoesNotExist:
            return None 

    def get_user(self, admin_id):
        try:
            return SurveyAdmin.objects.get(pk=admin_id)
        except SurveyAdmin.DoesNotExist:
            return None


class CustomTokenSerializer(TokenObtainPairSerializer):
    
    def login_admin(self, request : HttpRequest, survey_admin):
        refresh = self.get_token(survey_admin)
        tokens = {}
        tokens["refresh"] = str(refresh)
        tokens["access"] = str(refresh.access_token)
        
        return tokens

    
    
    