from typing import Optional
from main.models import Survey

class SurveyRepository:
    """
    Repository class for managing Survey instances.
    """
    survey_model = Survey
    
    @classmethod
    def get_by_id(cls, survey_id: int) -> Optional[Survey]:
        try:
            return cls.survey_model.objects.get(pk=survey_id)
        except cls.survey_model.DoesNotExist:
            return None
        
    @classmethod
    def get_by_title(cls, title: str) -> Optional[Survey]:
        try:
            return cls.survey_model.objects.get(title=title)
        except cls.survey_model.DoesNotExist:
            return None


    @classmethod
    def get_all_by_user(cls, admin) -> list[Survey]:
        return cls.survey_model.objects.filter(admin=admin)


    @classmethod
    def create(cls, admin, title: str, description: str, close_survey: bool = False) -> Survey:
        survey = cls.survey_model.objects.create(
            admin=admin,
            title=title, 
            description = description,
            close_survey=close_survey
            )
        survey.save()
        return survey
    

    @classmethod
    def update(cls, survey_id: int, **kwargs) -> Optional[Survey]:
        survey = cls.get_by_id(survey_id)
        if survey:
            for attr, value in kwargs.items():
                setattr(survey, attr, value)
            survey.save()
        return survey


    @classmethod
    def delete(cls, survey_id: int) -> bool:
        try:
            survey = cls.get_by_id(survey_id)
            if survey:
                survey.delete()
                return True
        except Exception:
            pass
        return False
