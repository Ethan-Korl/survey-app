from rest_framework.generics import ListCreateAPIView
from main.repository import QuestionRepository
from main.repository import SurveyRepository
from rest_framework.response import Response
from rest_framework import status
from main.serializers import QuestionListSerializer

que_repo = QuestionRepository
survey_repo = SurveyRepository


class GetQuetionsForSp(ListCreateAPIView):
    serializer_class = QuestionListSerializer

    def get(self, request, url_id):
        survey = survey_repo.get_by_url_id(url_id=url_id)
        questions = que_repo.get_by_survey(survey=survey)

        serializer = self.serializer_class(questions, many=True)
        data = {}
        data["survey"] = survey.title
        data["questions"] = serializer.data

        return Response(data=data, status=status.HTTP_200_OK)
