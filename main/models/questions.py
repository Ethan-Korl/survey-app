from django.utils import choices
from .surveys import Survey
from django.db import models

ANSWER_TPYES = [
    ("Text", "Text"),
    ("Selection", "Selection"),
    ("File", "File"),
    ("Image", "Image"),
    ("Number", "Number"),
]


class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question = models.TextField()
    type_of_response_required = models.CharField(choices=ANSWER_TPYES, max_length=50)
    max_length = models.PositiveIntegerField(null=True, blank=True)
    min_value = models.IntegerField(null=True, blank=True)
    max_value = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    answer_required = models.BooleanField(default=False)
