from rest_framework.serializers import ModelSerializer
from main.models import Question


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = (
            "survey",
            "question",
            "type_of_response_required",
        )
