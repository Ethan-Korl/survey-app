from rest_framework.serializers import (
    Serializer, 
    CharField,
    ModelSerializer
    )


class SurveyAdminSerializer(Serializer):
    username = CharField(max_length=50)
    password = CharField(max_length=100)