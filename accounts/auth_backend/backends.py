import jwt
from accounts.models import SurveyAdmin
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime, timedelta
from django.contrib.auth.base_user import AbstractBaseUser
from django.conf import settings
from django.http import HttpRequest
from accounts.models import SurveyAdmin
from accounts.repository import SurveyAdminRepository
from django.contrib.auth.hashers import make_password, check_password


sa_repo = SurveyAdminRepository

class BaseSurveyAdminManager(AbstractBaseUser):
    # for creating admin
    
    def _create_sa(self, username, password):
        _harshed_password = make_password(password)
        survey_admin = sa_repo.create(
                                username=username, 
                                password=_harshed_password,
                            )
        return survey_admin


       
class JWTBackend:
    def generate_jwt(sa_admin: SurveyAdmin):
        payload = {
            'user_id': str(sa_admin.admin_id),
            'exp': datetime.now() + timedelta(hours=1),
            'iat': datetime.now() 
        }
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
        return token

    def authenticate(self, request):
        token = request.headers.get('Authorization')
        if token is None:
            return None
        
        try:
            if token.startswith('Bearer '):
                token = token[7:]

            decoded = jwt.decode(token, settings.SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
            admin_id = decoded.get('admin_id')
            if admin_id is None:
                return None

            survey_admin = SurveyAdmin.objects.get(pk=admin_id)
            return survey_admin

        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError, ObjectDoesNotExist):
            return None

    def get_user(self, admin_id):
        try:
            return SurveyAdmin.objects.get(pk=admin_id)
        except SurveyAdmin.DoesNotExist:
            return None


class Authentication:
    jwt_backend = JWTBackend
    
    @classmethod
    def login(cls, request :HttpRequest, username, password) -> None:
        try:
            survey_admin = SurveyAdmin.objects.get(username=username)
            if check_password(password, survey_admin.password):
                auth_session = JWTBackend.generate_jwt(survey_admin)
                request.session["auth_session"] = auth_session
                pass
                # response.set_cookie('jwt', token, httponly=True, secure=True)
        except SurveyAdmin.DoesNotExist:
            return None

        token = cls.jwt_backend.generate_jwt(survey_admin)
    
    
    def logout(cls, request: HttpRequest):
        if request.COOKIES["auth_session"]:
            request.COOKIES["auth_session"] = None
            