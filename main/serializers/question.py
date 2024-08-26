from rest_framework.serializers import ModelSerializer
from main.models import Question


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = ("question", "type_of_reponse_required", "answer_Required")
