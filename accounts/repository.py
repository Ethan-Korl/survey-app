from accounts.models import SurveyAdmin
from typing import Optional
from django.db import models

class SurveyAdminRepository:
    """
    Repository class for managing SurveyAdmin instances.
    """
    sa = SurveyAdmin
    
    @classmethod
    def get_by_id(cls, admin_id: str) -> Optional[SurveyAdmin]:
        try:
            return cls.sa.objects.get(admin_id=admin_id)
        except cls.sa.DoesNotExist:
            return None

    @classmethod
    def get_by_username(cls, username: str) -> Optional[SurveyAdmin]:
        try:
            return cls.sa.objects.get(username=username)
        except cls.sa.DoesNotExist:
            return None

    @classmethod
    def create(cls, username: str, password: str) -> SurveyAdmin:
        admin = cls.sa.objects.create(username=username, password=password, is_active=True)
        admin.save()
        return admin
    

    @classmethod
    def update(cls, admin_id: str, **kwargs) -> Optional[SurveyAdmin]:
        admin = SurveyAdminRepository.get_by_id(admin_id)
        if admin:
            for attr, value in kwargs.items():
                setattr(admin, attr, value)
            admin.save()
        return admin


    @classmethod
    def delete(cls, admin_id: str) -> bool:
        try:
            admin = SurveyAdminRepository.get_by_id(admin_id)
            if admin:
                admin.delete()
                return True
        except Exception as e:
            pass
        return False
