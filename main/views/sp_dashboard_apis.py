from rest_framework.generics import ListCreateAPIView, CreateAPIView
from main.repository import SurveyRepository, OptionsRepository, QuestionRepository
from rest_framework.response import Response
from rest_framework import status
from main.serializers import (
    QuestionListSerializer,
    TextResponseSerializer,
    ImageResponseSerializer,
    FileResponseSerializer,
    SelectionResponseSerializer,
    NumberResponseSerializer,
)
from rest_framework.parsers import MultiPartParser
from rest_framework.exceptions import ValidationError

que_repo = QuestionRepository
survey_repo = SurveyRepository
option_repo = OptionsRepository


class GetQuetionsForSp(ListCreateAPIView):
    serializer_class = QuestionListSerializer

    def get(self, request, url_id):
        survey = survey_repo.get_by_url_id(url_id=url_id)
        questions = que_repo.get_by_survey(survey=survey)

        serializer = self.serializer_class(questions, many=True)
        data = {}
        data["survey"] = survey.title
        data["questions"] = []

        for question in questions:
            data["questions"].append(
                {
                    "survey": question.survey.pk,
                    "question": question.question,
                    "pk": question.pk,
                    "answer_required": question.answer_required,
                    "created_at": question.created_at,
                    "type_of_response_required": question.type_of_response_required,
                }
            )
            if question.type_of_response_required == "Selection":
                question_options = option_repo.get_by_question(question)
                data["questions"][len(data["questions"]) - 1]["options"] = [
                    {"question": op.question.pk, "option": op.option, "pk": op.pk}
                    for op in question_options
                ]
        return Response(data=data, status=status.HTTP_200_OK)


class CreateTextResponseView(CreateAPIView):
    serializer_class = TextResponseSerializer
    parser_classes = [MultiPartParser]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        try:
            if serializer.is_valid(raise_exception=True):
                res = serializer.validated_data.get("response")
                question_pk = serializer.validated_data.get("question").pk
                question = que_repo.get_by_id(question_id=question_pk)
                if len(res) > question.max_length:
                    raise ValidationError(
                        f"Response can not be more than {question.max_length} values"
                    )
                serializer.save()
                context = {"detail": "Text Response Added"}
                return Response(data=context, status=status.HTTP_201_CREATED)

        except ValidationError as ve:
            context = {"detail": ve.args[0]}
            print(ve.args[0])
            return Response(data=context, status=status.HTTP_400_BAD_REQUEST)

        return super().post(request, *args, **kwargs)


class CreateImageResponseView(CreateAPIView):
    serializer_class = ImageResponseSerializer
    parser_classes = [MultiPartParser]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        try:
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                context = {"detail": "Image Response Added"}
                return Response(data=context, status=status.HTTP_201_CREATED)

        except ValidationError as ve:
            context = {"detail": ve.default_detail}
            print(ve)
            return Response(data=context, status=status.HTTP_400_BAD_REQUEST)

        return super().post(request, *args, **kwargs)


class CreateFileResponseView(CreateAPIView):
    serializer_class = FileResponseSerializer
    parser_classes = [MultiPartParser]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        try:
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                context = {"detail": "File Response Added"}
                return Response(data=context, status=status.HTTP_201_CREATED)

        except ValidationError as ve:
            context = {"detail": ve.default_detail}
            print(ve)
            return Response(data=context, status=status.HTTP_400_BAD_REQUEST)

        return super().post(request, *args, **kwargs)


class CreateSelectionResponseView(CreateAPIView):
    serializer_class = SelectionResponseSerializer
    parser_classes = [MultiPartParser]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        try:
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(
                    {"detail": "Selection Response Added"},
                    status=status.HTTP_201_CREATED,
                )
        except ValidationError as ve:
            return Response(
                {"detail": ve.default_detail}, status=status.HTTP_400_BAD_REQUEST
            )


class CreateNumberResponseView(CreateAPIView):
    serializer_class = NumberResponseSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        try:
            if serializer.is_valid(raise_exception=True):
                res = serializer.validated_data.get("response")
                question_pk = serializer.validated_data.get("question").pk
                question = que_repo.get_by_id(question_id=question_pk)
                if int(res) > question.max_value or int(res) < question.min_value:
                    raise ValidationError(
                        f"Response not within ({question.min_value}, {question.max_value}) range"
                    )
                serializer.save()
                return Response(
                    {"detail": "Number Response Added"}, status=status.HTTP_201_CREATED
                )
        except ValidationError as ve:
            return Response({"detail": ve.args[0]}, status=status.HTTP_400_BAD_REQUEST)
