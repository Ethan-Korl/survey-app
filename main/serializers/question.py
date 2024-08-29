from rest_framework.serializers import ModelSerializer, SerializerMethodField
from main.models import Question


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = (
            "survey",
            "max_length",
            "min_value",
            "max_value",
            "question",
            "type_of_response_required",
        )


class QuestionListSerializer(ModelSerializer):
    # created_at = SerializerMethodField()

    class Meta:
        model = Question
        fields = (
            "survey",
            "question",
            "pk",
            "answer_required",
            "created_at",
            "type_of_response_required",
        )

    # def get_created_at(self, obj: Question):
    #     return obj.created_at.date
