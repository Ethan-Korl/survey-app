from django.db import models
from main.models.questions import Question


# for questions that have option
class Options(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option = models.CharField(max_length=50)


class TextResponse(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="text_responses"
    )
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)


class ImageResponse(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="image_responses"
    )
    response = models.ImageField(upload_to="ImageResponses")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)


class NumberResponse(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="number_responses"
    )
    response = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)


class FileResponse(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="file_responses"
    )
    response = models.FileField(upload_to="FileResponses")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)


class SelectionResponse(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="selection_responses"
    )
    response = models.ForeignKey(Options, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
