from django.utils import choices
from .surveys import Survey
from django.db import models

ANSWER_TPYES = [
    ("Text", "Text"),
    ("Selection", "Selection"),
    ("File", "File"),
    ("Image", "Image"),
]


class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question = models.TextField()
    type_of_response_required = models.CharField(choices=ANSWER_TPYES, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    answer_required = models.BooleanField(default=False)
