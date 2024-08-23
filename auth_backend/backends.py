import jwt
from accounts.models import SurveyAdmin
from django.conf import settings
from accounts.models import SurveyAdmin
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime, timedelta

class JWTBackend:
    def generate_jwt(sa_admin: SurveyAdmin):
        payload = {
            'user_id': sa_admin.admin_id,
            'exp': datetime.now() + timedelta(hours=1),
            'iat': datetime.now() 
        }
        token = jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
        return token

    def authenticate(self, request):
        token = request.headers.get('Authorization')
        if token is None:
            return None
        
        try:
            if token.startswith('Bearer '):
                token = token[7:]

            decoded = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user_id = decoded.get('user_id')
            if user_id is None:
                return None

            survey_admin = SurveyAdmin.objects.get(id=user_id)
            return survey_admin

        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError, ObjectDoesNotExist):
            return None

    def get_user(self, user_id):
        try:
            return SurveyAdmin.objects.get(pk=user_id)
        except SurveyAdmin.DoesNotExist:
            return None

