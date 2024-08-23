from inspect import classify_class_attrs
from django.db import models
from uuid import uuid4


class SurveyAdmin(models.Model):
    """
    Survey admin are the only users with login accesss
    """
    admin_id = models.UUIDField(default=uuid4, primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.TextField()
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)






