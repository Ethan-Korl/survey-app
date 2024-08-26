from django.shortcuts import render
from main.models import Survey, Question
from typing import Any
from main.repository import SurveyRepository, QuestionRepository
from main.serializers import (
    CreateSurveySerializer,
    ListSurveySerializer,
    QuestionSerializer,
    QuestionListSerializer,
)
from utils import check_if_required
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser
from rest_framework import status

survey_repo = SurveyRepository
ques_repo = QuestionRepository


class ListSurveyView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ListSurveySerializer

    def get(self, request, *args, **kwargs):
        surveys = survey_repo.get_all_by_user(request.user)
        serializer = self.serializer_class(surveys, many=True)
        data = {}
        data["surveys"] = serializer.data
        return Response(data=data, status=status.HTTP_200_OK)


class DeleteSurveyView(DestroyAPIView):

    def delete(self, request, survey_id):
        if survey_repo.delete(survey_id):
            return Response({"detail": "survey deleted"}, status=status.HTTP_200_OK)

        return Response({"detail": "survey not deleted"}, status=status.HTTP_200_OK)


class CreateQuestionView(CreateAPIView):
    serializer_class = QuestionSerializer
    parser_classes = [MultiPartParser]

    def post(self, request: Request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        try:
            if serializer.is_valid(raise_exception=True):
                survey = serializer.validated_data.get("survey")
                type_of_response_required = serializer.validated_data.get(
                    "type_of_response_required"
                )
                question = serializer.validated_data.get("question")
                answer_required = request.data.get("answer_required")

                ques_repo.create(
                    survey=survey,
                    question=question,
                    type_of_response_required=type_of_response_required,
                    answer_required=check_if_required(answer_required),
                )

                context = {"detail": "Question Added"}
                return Response(data=context, status=status.HTTP_200_OK)

        except ValidationError as ve:
            context = {"detail": ve.default_detail}
            print(ve)
            return Response(data=context, status=status.HTTP_400_BAD_REQUEST)

        return super().post(request, *args, **kwargs)


class ListQuestionView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = QuestionListSerializer

    def get(self, request, survey_id):
        surveys = ques_repo.get_by_survey(survey=survey_id)
        serializer = self.serializer_class(surveys, many=True)
        data = {}
        data["questions"] = serializer.data
        return Response(data=data, status=status.HTTP_200_OK)


class CreateSurveyView(CreateAPIView):
    parser_classes = [MultiPartParser]
    serializer_class = CreateSurveySerializer
    model_repo = SurveyRepository
    permission_classes = [IsAuthenticated]

    def post(self, request: Request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        try:
            if serializer.is_valid(raise_exception=True):
                title = serializer.validated_data.get("title")
                description = serializer.validated_data.get("description")

                # check if survey name already exits(title in this case)
                if self.model_repo.get_by_title(title=title) is not None:
                    context = {"detail": "Survey with the same name exists"}
                    return Response(data=context, status=status.HTTP_409_CONFLICT)

                survey = self.model_repo.create(
                    admin=request.user, title=title, description=description
                )
                context = {"detail": "Survey created"}
                return Response(data=context, status=status.HTTP_201_CREATED)

        except ValidationError as ve:
            context = {"detail": ve.default_detail}
            print(context)
            return Response(data=context, status=status.HTTP_400_BAD_REQUEST)

        return super().post(request, *args, **kwargs)
