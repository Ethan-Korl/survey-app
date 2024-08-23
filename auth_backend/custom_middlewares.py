import jwt
from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpRequest, JsonResponse
from accounts.models import SurveyAdmin

class JWTAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        # Extract the token from the Authorization header
        token = request.headers.get('Authorization')
        if token is None:
            request.survey_admin = None
        else:
            try:
                if token.startswith('Bearer '):
                    token = token[7:]

                # Decode the token
                decoded = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
                user_id = decoded.get('user_id')
                if user_id is not None:
                    request.survey_admin = SurveyAdmin.objects.get(id=user_id)
                else:
                    request.survey_admin = None

            except (jwt.ExpiredSignatureError, jwt.InvalidTokenError, User.DoesNotExist):
                request.survey_admin = None

        response = self.get_response(request)
        return response

