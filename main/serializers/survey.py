from rest_framework.serializers import ModelSerializer
from main.models import Survey

class CreateSurveySerializer(ModelSerializer):
    class Meta:
        model = Survey
        fields = (
            'title',
            'description',
        )
        

class SurveySerializer(ModelSerializer):
    class Meta:
        model = Survey
        fields = (
            'title',
            'description',
            'survey_url',
            'date_created',
        )