from django.http import HttpRequest
from django.shortcuts import render
from main.models import Survey, Question
from typing import Any
from main.repository import (
    SurveyRepository,
    QuestionRepository,
    OptionsRepository,
    ImageResponseRepository,
    FileResponseRepository,
    TextResponseRepository,
    SelectionResponseRepository,
    NumberResponseRepository,
)
from main.serializers import (
    CreateSurveySerializer,
    ListSurveySerializer,
    QuestionSerializer,
    QuestionListSerializer,
    OptionsSerializer,
    UpdateSurveySerializer,
)
from utils import check_if_required
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView,
)
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser
from rest_framework import status


survey_repo = SurveyRepository
ques_repo = QuestionRepository
option_repo = OptionsRepository


class ListSurveyView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ListSurveySerializer

    def get(self, request, *args, **kwargs):
        surveys = survey_repo.get_all_by_user(request.user)
        serializer = self.serializer_class(surveys, many=True)
        data = {}
        data["surveys"] = serializer.data
        return Response(data=data, status=status.HTTP_200_OK)


class CreateOptionsView(CreateAPIView):
    serializer_class = OptionsSerializer
    parser_classes = [MultiPartParser]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        try:
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                context = {"detail": "Option Added"}
                return Response(data=context, status=status.HTTP_201_CREATED)

        except ValidationError as ve:
            context = {"detail": ve.default_detail}
            print(ve)
            return Response(data=context, status=status.HTTP_400_BAD_REQUEST)

        return super().post(request, *args, **kwargs)


class ListOptionView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OptionsSerializer

    def get(self, request, question_id):
        options = option_repo.get_by_question(question=question_id)
        serializer = self.serializer_class(options, many=True)
        data = {}
        data["questions"] = serializer.data
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
                max_length = serializer.validated_data.get("max_length", None)
                min_value = serializer.validated_data.get("min_value", None)
                max_value = serializer.validated_data.get("max_value", None)

                question = serializer.validated_data.get("question")
                answer_required = request.data.get("answer_required")

                ques_repo.create(
                    survey=survey,
                    question=question,
                    min_value=min_value,
                    max_value=max_value,
                    max_length=max_length,
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
        questions = ques_repo.get_by_survey(survey=survey_id)
        serializer = self.serializer_class(questions, many=True)
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


class UpdateSurveyView(UpdateAPIView):
    parser_classes = [MultiPartParser]
    serializer_class = UpdateSurveySerializer
    model_repo = SurveyRepository
    permission_classes = [IsAuthenticated]

    def patch(self, request, survey_id):
        survey = self.model_repo.get_by_id(survey_id)
        serializer = self.serializer_class(survey, data=request.data, partial=True)
        try:
            if serializer.is_valid(raise_exception=True):
                self.perform_update(serializer)
                return Response(
                    data={"detail": "Survey  Updated"}, status=status.HTTP_200_OK
                )
        except ValidationError as ve:
            context = {"detail": ve.default_detail}
            print(context)
            return Response(data=context, status=status.HTTP_400_BAD_REQUEST)


class ListQuestionResponse(ListAPIView):
    permission_classes = [IsAuthenticated]

    _img_repo = ImageResponseRepository
    _sel_repo = SelectionResponseRepository
    _txt_repo = TextResponseRepository
    _file_repo = FileResponseRepository
    _num_repo = NumberResponseRepository
    data = []

    def add_response(self, reponses):
        for rep in reponses:
            self.data.append(
                {
                    "response": rep.response,
                    "created_at": f"{rep.created_at.date()} || {rep.created_at.time()}",
                }
            )

    def get(self, request: HttpRequest, question_id):
        # clear previous state of the data attribute on every request
        self.data.clear()
        question = ques_repo.get_by_id(question_id)
        if question.type_of_response_required == "Selection":
            reponses = self._sel_repo.get_by_question(question)
            for rep in reponses:
                self.data.append(
                    {
                        "response": rep.response.option,
                        "created_at": f"{rep.created_at.date()} || {rep.created_at.time()}",
                    }
                )

        if question.type_of_response_required == "Text":
            reponses = self._txt_repo.get_by_question(question)
            self.add_response(reponses)

        if question.type_of_response_required == "Image":
            reponses = self._img_repo.get_by_question(question)
            print(reponses)
            for rep in reponses:
                self.data.append(
                    {
                        "response": f"https://{request.get_host()}{rep.response.url}",
                        "created_at": f"{rep.created_at.date()} || {rep.created_at.time()}",
                    }
                )

        if question.type_of_response_required == "File":
            reponses = self._file_repo.get_by_question(question)
            for rep in reponses:
                self.data.append(
                    {
                        "response": f"https://{request.get_host()}{rep.response.url}",
                        "created_at": f"{rep.created_at.date()} || {rep.created_at.time()}",
                    }
                )

        if question.type_of_response_required == "Number":
            reponses = self._num_repo.get_by_question(question)
            self.add_response(reponses)

        return Response(data=self.data, status=status.HTTP_200_OK)
