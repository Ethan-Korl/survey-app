from inspect import classify_class_attrs
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from uuid import uuid4
from django.contrib.auth.hashers import make_password
from django.contrib.auth.base_user import BaseUserManager

class SurveyAdmin(AbstractBaseUser):
    """
    Survey admin are the only users with login accesss
    """
    id = models.UUIDField(default=uuid4, primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.TextField()
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(null=True, blank=True)
    
    
    USERNAME_FIELD = "username"
    
    class Meta:
        db_table = "survey_admin"
    
    
    





