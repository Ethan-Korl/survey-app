from rest_framework.serializers import ModelSerializer, CharField, Serializer
from main.models import Survey


class ListSurveySerializer(ModelSerializer):
    class Meta:
        model = Survey
        fields = ("pk", "url_id", "title", "description", "survey_link")


class CreateSurveySerializer(Serializer):
    title = CharField(max_length=50)
    description = CharField(max_length=200)


class UpdateSurveySerializer(ModelSerializer):
    class Meta:
        model = Survey
        fields = (
            "title",
            "description",
        )


class SurveySerializer(ModelSerializer):
    class Meta:
        model = Survey
        fields = (
            "title",
            "description",
            "survey_url",
            "date_created",
        )
