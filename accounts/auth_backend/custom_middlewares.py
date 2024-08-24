import jwt
from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpRequest, JsonResponse
from accounts.models import SurveyAdmin

class JWTAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        # Extract the token from the Authorization session
        token = request.session.get('auth_session')
        if token is None:
            request.survey_admin = None
        else:
            try:
                decoded = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
                admin_id = decoded.get('admin_id')
                if admin_id is not None:
                    request.survey_admin = SurveyAdmin.objects.get(pk=admin_id)
                else:
                    request.survey_admin = None

            except (jwt.ExpiredSignatureError, jwt.InvalidTokenError, User.DoesNotExist):
                request.survey_admin = None

        response = self.get_response(request)
        return response

