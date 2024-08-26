from rest_framework import serializers
from main.models import (
    Options,
    TextResponse,
    ImageResponse,
    FileResponse,
    SelectionResponse,
)


class OptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Options
        fields = "__all__"


class TextResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextResponse
        fields = "__all__"


class ImageResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageResponse
        fields = "__all__"


class FileResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileResponse
        fields = "__all__"


class SelectionResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelectionResponse
        fields = "__all__"
