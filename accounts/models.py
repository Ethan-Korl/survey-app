from inspect import classify_class_attrs
from django.db import models
from uuid import uuid4
from django.contrib.auth.hashers import make_password


class BaseSurveyAdminManager:
    # for creating admin
    def _create_sa(self, username, password):
        _harshed_password = make_password(password=password)
        survey_admin =SurveyAdmin.objects.create(
                                username=username, 
                                password=_harshed_password
                            )
        survey_admin.save()



class SurveyAdmin(models.Model, BaseSurveyAdminManager):
    """
    Survey admin are the only users with login accesss
    """
    admin_id = models.UUIDField(default=uuid4, primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.TextField()
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    
    def create_survey_admin(self, username, password):
        return super()._create_sa(username, password)






