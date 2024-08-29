from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from accounts.models import SurveyAdmin
from django.urls import reverse
from rest_framework.views import APIView
from accounts.repository import SurveyAdminRepository
from auth_backend.backends import (
    BaseSurveyAdminManager,
    CustomTokenSerializer,
    SimpleAuthBackend,
)
from accounts.serializers import SurveyAdminSerializer, SurveyAdminLoginSerializer
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.exceptions import ValidationError
from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.response import Response
from accounts.serializers import SurveyAdminSerializer

# from django.
# Create your views here.


sa_repo = SurveyAdminRepository


class RegisterView(APIView):

    parser_classes = [MultiPartParser]

    serializer_class = SurveyAdminSerializer

    def get(self, request, *args, **kwargs):
        return render(request, "sa_register.html")

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        try:
            if serializer.is_valid(raise_exception=True):
                username = serializer.validated_data.get("username")
                password = serializer.validated_data.get("password")
                confirm_password = serializer.validated_data.get("confirm_password")

                if sa_repo.get_by_username(username) is not None:
                    context = {"detail": "username already"}
                    return Response(data=context, status=status.HTTP_409_CONFLICT)

                if not (password == confirm_password):
                    context = {"detail": "password not matching"}
                    return Response(data=context, status=status.HTTP_400_BAD_REQUEST)

                survey_admin = BaseSurveyAdminManager.create_survey_admin(
                    username=username, password=password
                )

                tokens = CustomTokenSerializer().login_admin(request, survey_admin)
                tokens["dashboard_url"] = reverse("sa-dashboard")
                return Response(data=tokens, status=status.HTTP_200_OK)

        except ValidationError as ve:
            print(ve.detail)
            context = {"detail": ve.default_detail}
            return Response(data=context, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):

    parser_classes = [MultiPartParser]

    serializer_class = SurveyAdminLoginSerializer

    def get(self, request, *args, **kwargs):
        return render(request, "sa_login.html")

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        try:
            if serializer.is_valid(raise_exception=True):
                username = serializer.validated_data.get("username")
                password = serializer.validated_data.get("password")

                admin = SimpleAuthBackend.authenticate(
                    username=username, password=password
                )
                if admin is None:
                    context = {"detail": "Invalid username or password"}
                    return Response(data=context, status=status.HTTP_400_BAD_REQUEST)

                tokens = CustomTokenSerializer().login_admin(request, admin)
                tokens["dashboard_url"] = reverse("sa-dashboard")
                return Response(data=tokens, status=status.HTTP_200_OK)

        except ValidationError as ve:
            print(ve.detail)
            context = {"detail": ve.default_detail}
            return Response(data=context, status=status.HTTP_400_BAD_REQUEST)
